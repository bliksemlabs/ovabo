import json

from operator import __or__ as OR
from operator import __and__ as AND
from django.db.models import QuerySet, Q
from django.views.generic import ListView

from data.models import Line
from django.core.cache import cache

from utils.views import JSONListResponseMixin


class MissingPriceDataReport(ListView):
    model = Line
    ordering = ['dataownercode', 'lineplanningnumber']

    def get_queryset(self):
        qry = super(MissingPriceDataReport, self).get_queryset()
        return qry.filter(ppt_id__isnull=True)

    def get_context_data(self, **kwargs):
        ctx = super(MissingPriceDataReport, self).get_context_data(**kwargs)
        ctx['total'] = self.model.objects.all().count()
        return ctx


class MissingPriceDataLinesView(JSONListResponseMixin, ListView):
    model = Line
    render_object = 'object_list'

    def get_queryset(self):
        qry = super(MissingPriceDataLinesView, self).get_queryset()
        qry = qry.filter(ppt_id__isnull=True).exclude(transportmode=1)
        line_list = qry.values('pk', 'dataownercode', 'headsign', 'lineplanningnumber', 'publiclinenumber', 'json_lines')
        for r in line_list:
            r['json_lines'] = json.loads(r['json_lines'])
        return line_list


class LineSearchView(JSONListResponseMixin, ListView):
    model = Line
    render_object = 'object_list'

    def get_queryset(self):
        qry = super(LineSearchView, self).get_queryset()
        needle = unicode(self.request.GET.get('search', ''))
        dataowner = self.request.GET.get('dataownercode', None)
        qry = qry.filter(Q(headsign__icontains=needle) | Q(publiclinenumber__startswith=needle) | Q(lineplanningnumber__startswith=needle) )\
            .order_by('lineplanningnumber')
        if dataowner is not None:
            qry = qry.filter(dataownercode=dataowner)
        return qry.values('pk', 'dataownercode', 'headsign', 'lineplanningnumber', 'publiclinenumber', 'json_lines')


class AdvancedLineSearchView(JSONListResponseMixin, ListView):
    model = Line
    render_object = 'object_list'

    def get_queryset(self):
        qry = super(AdvancedLineSearchView, self).get_queryset()
        needle = unicode(self.request.GET.get('search', '').replace('*', '%'))
        cached = cache.get('line-search_%s' % needle)
        if cached:
            return cached

        groups = needle.split(',')
        include = [self.add_filters(g) for g in groups if g != "" and g[0] != '!']
        exclude = [self.add_filters(g[1:]) for g in groups if g != "" and g[0] == '!']

        # TODO: Do something with exclude
        # .exclude(reduce(OR, exclude))
        qry = qry.filter(reduce(OR, include)).order_by('lineplanningnumber')

        line_list = qry.values('pk', 'dataownercode', 'headsign', 'lineplanningnumber', 'publiclinenumber', 'json_lines')
        for r in line_list:
            r['json_lines'] = json.loads(r['json_lines'])
        cache.set('line-search_%s' % needle, line_list)
        return line_list

    # TODO: Move this to model
    def add_filters(self, group):
        parts = group.split(':')
        q = Q(self.get_kwarg(parts[0], 'dataownercode'))

        if len(parts) > 1:
            q.add(self.get_kwarg(parts[1], 'lineplanningnumber'), Q.AND)

        return q

    # TODO: Move this to manager
    def get_kwarg(self, value, field):
        if "%" in value:
            if value[-1] == '%' and value[0] == '%':
                field += '__contains'
            elif value[-1] == '%':
                field += '__startswith'
            else:
                field += '__endswith'
            value = value.replace('%', '')
        return Q(**{field: value})