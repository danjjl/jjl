# -*- coding: utf-8 -*-
from django.forms import Form, ModelForm, FileField, IntegerField, HiddenInput
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, Div, Field

from JJL.Peoulot.models import Peoula

class PeoulaForm(ModelForm):
    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(
                Fieldset(
                    '',
                    'nom', 'age', 'duree', 'theme', 'genre', 'but',
                    css_class="well",
                ),
                Fieldset(
                    'Commentaires & modifications',
                    'commentaires', 'variantes',
                ),
                css_class="container pull-right col-md-5 col-xs-12",
            ),
            Div(
                Fieldset(
                    '',
                    'introduction', 'deroulement', 'conclusion', 'materiel',
                ),
                css_class="container col-md-7 col-xs-12",
            ),
        )
        super(PeoulaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Peoula
        exclude = ('date_creation', 'telechargement')

class UploadFileForm(Form):
    file = FileField(required=False)

    def __init__(self, *args, **kwargs):
        self.helper = FormHelper()
        self.helper.html5_required = True
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Field('file', css_class="multi")
        )
        super(UploadFileForm, self).__init__(*args, **kwargs)

class DeletePeoulaForm(Form):
    pk = IntegerField(required=True, widget=HiddenInput())
