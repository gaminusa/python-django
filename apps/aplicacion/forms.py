# -*- coding:utf-8 -*-

from django import forms
from django.forms import widgets
from aplicacion import constants
from .models import Inscrito, Pata


class DocumentoValidationForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ('num_doc', 'tipo_doc')


class NuevoRegistroForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = ('nombres', 'apellido_paterno', 'apellido_materno', 'fec_nac',
                  'tipo_doc', 'num_doc', 'sexo', 'email', 'celular', 'ubigeo')


class RegistroPataForm(forms.ModelForm):
    mayor_edad = forms.ChoiceField(
        choices=constants.CHOICES_EDAD,
        widget=forms.RadioSelect()
    )

    class Meta:
        model = Pata
        fields = ('nombres', 'mayor_edad', 'ubigeo', 'direccion',
                  'referencia', 'cel')


class MensajePata(forms.ModelForm):
    class Meta:
        model = Pata
        widgets = {
            'mensaje': forms.Textarea(attrs={'cols': 200, 'rows': 200}),
        }
