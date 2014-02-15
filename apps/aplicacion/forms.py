# -*- coding:utf-8 -*-

from django import forms
from .models import Inscritos

class DocumentoValidationForm(forms.ModelForm):
    num_doc = forms.CharField(required=True,max_length=15, min_length=8)
    tipo_doc