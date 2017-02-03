from django.db.models import QuerySet
from django.forms import inlineformset_factory
from django.http import JsonResponse
from django.shortcuts import redirect
from django.views.generic import RedirectView
from django.views.generic.detail import SingleObjectMixin
from django.views.generic.edit import ModelFormMixin


class JSONResponseMixin(object):
    """
    A mixin that can be used to render a JSON response.
    """
    def render_json_response(self, context, **response_kwargs):
        """
        Returns a JSON response, transforming 'context' to make the payload.
        """
        return JsonResponse(
            self.get_data(context),
            **response_kwargs
        )

    def get_data(self, context):
        """
        Returns an object that will be serialized as JSON by json.dumps().
        """
        # Note: This is *EXTREMELY* naive; in reality, you'll need
        # to do much more complex handling to ensure that arbitrary
        # objects -- such as Django model instances or querysets
        # -- can be serialized as JSON.
        return context


class JSONListResponseMixin(JSONResponseMixin):
    render_object = None  # Name of thing to get from context object

    def render_to_response(self, context):
        contents = {}
        if self.render_object:
            if isinstance(context[self.render_object], QuerySet):
                contents[self.render_object] = list(context[self.render_object])
            else:
                contents[self.render_object] = context[self.render_object]
        return self.render_json_response(contents)


class SingleFormsetMixin(ModelFormMixin):
    inline_model = None
    inline_form_class = None
    inline_extras = 0

    inline_context_name = 'inline'

    def get_formset(self):
        return inlineformset_factory(self.model, self.inline_model, extra=self.inline_extras, can_delete=True,
                                     form=self.inline_form_class)

    def get_context_data(self, **kwargs):
        ctx = super(SingleFormsetMixin, self).get_context_data(**kwargs)
        formset = self.get_formset()
        if self.request.POST:
            ctx[self.inline_context_name] = formset(self.request.POST, instance=self.get_object())
        else:
            ctx[self.inline_context_name] = formset(instance=self.get_object())
        return ctx

    def form_valid(self, form):
        ctx = self.get_context_data()
        if ctx[self.inline_context_name].is_valid() and form.is_valid():
            self.object = form.save()
            ctx[self.inline_context_name].save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))


class MultipleFormsetsMixin(ModelFormMixin):
    """
    Use to have multiple formsets automagically in a form. do_formset_save() can be overridden for custom logic
    'inlines' is a tuple of context name, model, form class and number of extra forms
    Example for inlines: [('product_reductions', ProductReduction, ProductReductionForm, 1),]
    """
    # TODO: Make all options configurable
    inlines = []

    def get_formsets(self):
        return {i[0]: self.get_formset(i[1], i[2], extra=i[3]) for i in self.inlines}

    def get_formset(self, inline_model, inline_form_class, extra=1):
        return inlineformset_factory(self.model, inline_model, extra=extra, can_delete=True, form=inline_form_class)

    def get_context_data(self, **kwargs):
        ctx = super(MultipleFormsetsMixin, self).get_context_data(**kwargs)
        self.formsets = self.get_formsets()
        for key, formset in self.formsets.items():
            if self.request.POST:
                ctx[key] = formset(self.request.POST, instance=self.get_object())
            else:
                ctx[key] = formset(instance=self.get_object())
        return ctx

    def form_valid(self, form):
        self.context = self.get_context_data()
        # Check all the formsets are valid
        formsets_valid = True
        for key, formset in self.formsets.iteritems():
            if not self.context[key].is_valid():
                formsets_valid = False

        if formsets_valid and form.is_valid():
            self.object = form.save()
            self.do_formset_save()
            return redirect(self.get_success_url())
        else:
            return self.render_to_response(self.get_context_data(form=form))

    def do_formset_save(self):
        for key, formset in self.formsets.iteritems():
            self.context[key].save()


class CloneView(SingleObjectMixin, RedirectView):

    def post(self, request, *args, **kwargs):
        self.get_object().clone()
        return super(CloneView, self).post(request, *args, **kwargs)