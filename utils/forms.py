from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Field
from django import forms


class BaseBootstrapModelForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(BaseBootstrapModelForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.label_class = 'col-lg-2'
        self.helper.field_class = 'col-lg-4'


class BaseNotesForm(BaseBootstrapModelForm):
    """ Two columns with name left & notes right"""

    def __init__(self, *args, **kwargs):
        super(BaseNotesForm, self).__init__(*args, **kwargs)
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-9'
        self.helper.layout = Layout(
            Div(
                Div(Field('description'), css_class="col-md-5"),
                Div(Field('notes'), css_class="col-md-7"),
                css_class="row")
        )