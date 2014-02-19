# -*- coding: utf-8 -*-
"""
field and widget for Ubigeo Field
"""

from django.forms.widgets import MultiWidget, Select

from django.forms import ModelChoiceField

from django import forms

from ubigeo.models import Ubigeo
from django.template.loader import render_to_string


class UbigeoWidget(forms.MultiWidget):
    """
    Widget to draw three selects for ubigeo, department, province and district
    """
    def __init__(self, attrs=None, *args, **kwargs):
        departments = self.get_department()        
        provinces = self.get_province(departments[0][0])        
        districts = self.get_district(provinces[0][0])
        widgets = (
                Select(choices = departments, attrs={'name':'department','id':'department',}),
                Select(choices = provinces, attrs={'name':'province','id':'department',}),
                Select(choices = districts, attrs={'name':'distric','id':'department',})
                ,)
        super(UbigeoWidget, self).__init__(widgets,attrs)

    def render(self, name, value, attrs=None):
        return render_to_string("ubigeo/ubigeo_ajax.html",{'widgets':self.widgets})

    class Media:
        try:
            js  = (
                     'js/jquery.min.js',
                  )
        except AttributeError:
            pass 

    def get_department(self):
        departments = Ubigeo.objects.values_list('id','name').filter(parent__isnull=True)
        return departments

    def get_province(self, department):
        province = Ubigeo.objects.values_list('id','name').filter(parent=department)
        return province

    def get_district(self, province):
        district = Ubigeo.objects.values_list('id','name').filter(parent=province)
        return district


class UbigeoField(forms.MultiValueField):
    """
    """
    def __init__(self, *args, **kwargs):
        forms.MultiValueField.__init__(self, *args, **kwargs)
        self.fields = (forms.CharField(), forms.CharField(),forms.CharField(),)


class UbigeoForm(forms.ModelForm):
    """
    """
    ubigeo = UbigeoField(widget=UbigeoWidget())
    
    class Meta:
		model = Ubigeo
