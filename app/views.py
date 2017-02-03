from django.core.urlresolvers import reverse_lazy
from django.views.generic import UpdateView, ListView, CreateView

from app.forms import AddProductForm, EditProductForm, ProductReductionForm, LineGroupForm, LineForm, \
    TemporalAvailabilityForm, WeekdayForm, AgeGroupForm, AgeForm, ProductBearerForm, ProductPriceForm, \
    ProductAvailabilityForm, ProductValidityForm, ProductLocationForm, ProductValidityPeriodForm, \
    ProductValidityRuleForm, ProductSellerForm, SellerForm
from app.models import Product, ProductReduction, LineGroup, TemporalAvailability, Line, Weekdays, AgeGroup, Age, \
    ProductBearer, ProductPrice, ProductAvailability, ProductValidity, ProductLocation, ProductValidityPeriod, \
    ProductValidityRule, ProductSeller, Seller
from data.models import DATAOWNERCODE
from utils.views import SingleFormsetMixin, CloneView, MultipleFormsetsMixin


class ListProductView(ListView):
    model = Product


class CreateProductView(CreateView):
    model = Product
    form_class = AddProductForm

    def get_success_url(self):
        return reverse_lazy('product_edit', kwargs={'pk': self.object.pk})


class UpdateProductView(UpdateView, MultipleFormsetsMixin):
    model = Product
    form_class = EditProductForm
    success_url = reverse_lazy('product_list')

    inlines = [('product_reductions', ProductReduction, ProductReductionForm, 1),
               ('bearers', ProductBearer, ProductBearerForm, 0),
               ('prices', ProductPrice, ProductPriceForm, 0),
               ('validities', ProductValidity, ProductValidityForm, 0),
               ('validity_periods', ProductValidityPeriod, ProductValidityPeriodForm, 0),
               ('validity_rules', ProductValidityRule, ProductValidityRuleForm, 0),
               ('availabilities', ProductAvailability, ProductAvailabilityForm, 0),
               ('locations', ProductLocation, ProductLocationForm, 0),
               ('sellers', ProductSeller, ProductSellerForm, 0),
               ]

    def form_valid(self, form):
        form.instance.validated = False  # Editing the object clears validation status (in the future add some diff detection)
        return super(UpdateProductView, self).form_valid(form)


class CloneProductView(CloneView):
    model = Product
    url = reverse_lazy('product_list')


class ListLineView(ListView):
    model = LineGroup


class CreateLineView(CreateView):
    model = LineGroup
    form_class = LineGroupForm

    def get_success_url(self):
        return reverse_lazy('line_edit', kwargs={'pk': self.object.pk})


class UpdateLineView(UpdateView, SingleFormsetMixin):
    model = LineGroup
    form_class = LineGroupForm
    success_url = reverse_lazy('line_list')

    inline_model = Line
    inline_form_class = LineForm
    inline_context_name = 'lines'

    def get_context_data(self, **kwargs):
        ctx = super(UpdateLineView, self).get_context_data(**kwargs)
        ctx['dataownercode'] = DATAOWNERCODE
        return ctx

    def form_valid(self, form):
        form.instance.validated = False # Editing the object clears validation status (in the future add some diff detection)
        return super(UpdateLineView, self).form_valid(form)


class CloneLineView(CloneView):
    model = LineGroup
    url = reverse_lazy('line_list')


class ListCalendarView(ListView):
    model = TemporalAvailability


class CreateCalendarView(CreateView):
    model = TemporalAvailability
    form_class = TemporalAvailabilityForm

    def get_success_url(self):
        return reverse_lazy('calendar_edit', kwargs={'pk': self.object.pk})


class UpdateCalendarView(UpdateView, SingleFormsetMixin):
    model = TemporalAvailability
    form_class = TemporalAvailabilityForm
    success_url = reverse_lazy('calendar_list')

    inline_model = Weekdays
    inline_form_class = WeekdayForm
    inline_context_name = 'weekdays'


class CloneCalendarView(CloneView):
    model = TemporalAvailability
    url = reverse_lazy('calendar_list')


class ListAgeGroupView(ListView):
    model = AgeGroup


class CreateAgeGroupView(CreateView):
    model = AgeGroup
    form_class = AgeGroupForm

    def get_success_url(self):
        return reverse_lazy('agegroup_edit', kwargs={'pk': self.object.pk})


class UpdateAgeGroupView(UpdateView, SingleFormsetMixin):
    model = AgeGroup
    form_class = AgeGroupForm
    success_url = reverse_lazy('agegroup_list')

    inline_model = Age
    inline_form_class = AgeForm
    inline_context_name = 'ages'


class CloneAgeGroupView(CloneView):
    model = AgeGroup
    url = reverse_lazy('agegroup_list')


class ListSellerView(ListView):
    model = Seller


class CreateSellerView(CreateView):
    model = Seller
    form_class = SellerForm
    success_url = reverse_lazy('seller_list')


class UpdateSellerView(UpdateView):
    model = Seller
    form_class = SellerForm
    success_url = reverse_lazy('seller_list')

