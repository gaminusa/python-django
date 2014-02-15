from django.http import HttpResponse

__author__ = 'gnurenia'
# -*- coding: utf-8 -*-

from aplicacion.models import Inscrito
from django.views.generic import TemplateView, View


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hola mundo')


class ValidarView(TemplateView):
    template_name = 'pilsen/validar.html'

    def get_context_data(self, **kwargs):
        context = super(ValidarView, self).get_context_data(**kwargs)
        context['inscritos'] = Inscrito.objects.all()
        return context


class RegistroNuevoView(TemplateView):
    template_name = 'pilsen/nuevo_registro.html'
