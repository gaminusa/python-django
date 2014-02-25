# -*- coding:utf-8 -*-
from django.contrib import admin
from aplicacion.forms import MensajePata
from aplicacion.models import Inscrito, Pata


class InscritoAdmin(admin.ModelAdmin):
    list_display = (
        'num_doc', 'nombres', 'apellido_paterno', 'apellido_materno', 'sexo', 'fec_nac', 'email', 'direccion',
        'telefono', 'celular', 'ubigeo')
    list_filter = ('tipo_doc',)


class PataAdmin(admin.ModelAdmin):
    list_display = (
        'nombres', 'direccion', 'cel', 'referencia', 'dni_inscrito', 'mensaje'
    )
    list_filter = ('dni_inscrito',)
    form = MensajePata

    class Media:
        js = [
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/js/tinymce_setup.js',
            '/static/js/jquery.1.10.2.min.js',

        ]


admin.site.register(Inscrito, InscritoAdmin)
admin.site.register(Pata, PataAdmin)