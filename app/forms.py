from crispy_forms.bootstrap import PrependedText, AppendedText, FieldWithButtons, StrictButton, InlineRadios
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Submit, Div, HTML
from django import forms
from django.core.urlresolvers import reverse

from app.models import Product, ProductReduction, LineGroup, Line, TemporalAvailability, Weekdays, AgeGroup, Age, \
    ProductBearer, ProductPrice, ProductAvailability, ProductValidity, ProductLocation, ProductValidityPeriod, \
    ProductValidityRule, ProductSeller, Seller
from utils.forms import BaseBootstrapModelForm, BaseNotesForm


class AddProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name']

    def __init__(self, *args, **kwargs):
        super(AddProductForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_class = 'form-horizontal'
        self.helper.form_action = reverse('product_add')
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-6'
        self.helper.layout = Layout(
            Field('name'),
            Submit('add', 'Toevoegen', css_class='btn-primary pull-right'),
        )


# TODO: these should probably extend each other
class EditProductForm(BaseBootstrapModelForm):
    class Meta:
        model = Product
        fields = ['name', 'identifier', 'notes', 'product_director', 'product_owner', 'validated', 'incomplete']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 5}),
        }

    def __init__(self, *args, **kwargs):
        super(EditProductForm, self).__init__(*args, **kwargs)
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Div(
                Div(Field('identifier'), css_class="col-md-6"),
                css_class="row"),
            Div(
                Div(Field('name'), css_class="col-md-6"),
                Div(Field('notes'), css_class="col-md-6"),
                css_class="row"),
            Div(
                Div(Field('product_owner'), css_class="col-md-6"),
                Div(Field('validated'), css_class="col-md-6"),
                css_class="row"
            ),
            Div(
                Div(Field('product_director'), css_class="col-md-6"),
                Div(Field('incomplete'), css_class="col-md-6"),
                css_class="row"
            )
        )


class ProductReductionForm(BaseBootstrapModelForm):
    class Meta:
        model = ProductReduction
        exclude = ['description']

    def __init__(self, *args, **kwargs):
        super(ProductReductionForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Field('id', hidden=True),
            AppendedText('reduction', '%'),
            FieldWithButtons('linegroup', StrictButton('<i class="glyphicon glyphicon-plus"></i>&nbsp;' + "Toevoegen",
                                                  css_class="btn btn-success btn_edit_linegroup")),
            FieldWithButtons('temporaryavailability', StrictButton('<i class="glyphicon glyphicon-plus"></i>&nbsp;' + "Toevoegen",
                                                        css_class="btn btn-success btn_edit_temporalavailability")),
            Field('DELETE')  # TODO: Figure out why this is needed here and not elsewhere
        )


class ProductBearerForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductBearer
        fields = ['bearer']


class ProductValidityForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductValidity
        fields = ['validity_type', 'number']


class ProductValidityPeriodForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductValidityPeriod
        fields = ['type', 'valid_from', 'valid_to']


class ProductValidityRuleForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductValidityRule
        fields = ['rule', 'allowed', 'value']

    def __init__(self, *args, **kwargs):
        super(ProductValidityRuleForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Field('id', hidden=True),
            Field('rule'),
            InlineRadios('allowed'),
            Field('value'),
            Field('DELETE')  # TODO: Figure out why this is needed here and not elsewhere
        )


class ProductAvailabilityForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductAvailability
        fields = ['available_from', 'available_to']


class ProductLocationForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductLocation
        fields = ['location_type', 'online_url']


class ProductSellerForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductSeller
        fields = ['seller']


class ProductPriceForm(BaseBootstrapModelForm):

    class Meta:
        model = ProductPrice
        fields = ['duration', 'price', 'age_group']

    def __init__(self, *args, **kwargs):
        super(ProductPriceForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
                Field('id', hidden=True),
                Field('duration'),
                PrependedText('price', '&euro;'),
                Field('age_group'),
                Field('DELETE')
        )


class LineGroupForm(BaseNotesForm):

    class Meta:
        model = LineGroup
        fields = ['description', 'notes', 'validated', 'incomplete']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }

    def __init__(self, *args, **kwargs):
        super(LineGroupForm, self).__init__(*args, **kwargs)
        self.helper.layout = Layout(
            Div(
                Div(Field('description'), css_class="col-md-5"),
                Div(Field('notes'), css_class="col-md-7"),
                css_class="row"),
            Div(
                Div(css_class="col-md-5"),
                Div(Field('validated'), Field('incomplete'), css_class="col-md-7"),
                css_class="row")
        )


class LineForm(BaseBootstrapModelForm):

    class Meta:
        model = Line
        fields = ['type', 'pattern']  # 'transportmode'

    def __init__(self, *args, **kwargs):
        super(LineForm, self).__init__(*args, **kwargs)
        self.helper.field_class = 'col-lg-10'


class TemporalAvailabilityForm(BaseNotesForm):

    class Meta:
        model = TemporalAvailability
        fields = ['description', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class WeekdayForm(BaseBootstrapModelForm):

    class Meta:
        model = Weekdays
        fields = ['weekday', 'from_time', 'to_time']


class AgeGroupForm(BaseNotesForm):

    class Meta:
        model = AgeGroup
        fields = ['description', 'notes']
        widgets = {
            'notes': forms.Textarea(attrs={'rows': 3}),
        }


class AgeForm(BaseBootstrapModelForm):

    class Meta:
        model = Age
        fields = ['from_age', 'end_age']


class SellerForm(BaseBootstrapModelForm):

    class Meta:
        model = Seller
        fields = ['name', 'phone', 'url']