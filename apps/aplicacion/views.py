# -*- coding: utf-8 -*-
from django.contrib.formtools.wizard.views import CookieWizardView
from django.core.urlresolvers import reverse
from django.shortcuts import redirect
from django.utils.timezone import now

from aplicacion.models import Inscrito, PromocionesInscritos
from django.views.generic import TemplateView, View, FormView
from django.http import HttpResponse
from aplicacion.forms import DocumentoValidationForm, NuevoRegistroForm, RegistroPataForm, MensajePata
from django.conf import settings


class IndexView(View):
    def get(self, request, *args, **kwargs):
        return HttpResponse('hola mundo')


class ValidarView(FormView):
    template_name = 'pilsen/validar.html'
    form_class = DocumentoValidationForm

    def form_valid(self, form):
        num_doc = form.cleaned_data['num_doc']
        tipo_doc = form.cleaned_data['tipo_doc']

        # consulta
        value = Inscrito.objects.filter(
            tipo_doc=tipo_doc, num_doc=num_doc).using('default').exists()

        # si existe
        if value:
            return redirect('pata')
        # si no
        else:
            return redirect('registro')


class RegistraProcesoWizardView(CookieWizardView):
    form_list = [NuevoRegistroForm, RegistroPataForm, MensajePata]

    def get_template_names(self):
        if self.steps.step0 == 0:
            return 'pilsen/nuevo_registro.html'
        elif self.steps.step0 == 1:
            return 'pilsen/registro_pata.html'
        elif self.steps.step0 == 2:
            return 'pilsen/mensaje.html'

    def done(self, form_list, **kwargs):
        nuevo_registro = form_list[0]
        registro_pata = form_list[1]
        mensaje_pata = form_list[2]

        nuevo = nuevo_registro.save()
        pata = registro_pata.save(commit=False)
        pata.dni_inscrito = nuevo.num_doc
        pata.save()
        pro_inscr = PromocionesInscritos(dni=nuevo.num_doc)
        pro_inscr.save()
        mensaje = mensaje_pata.save(commit=False)
        pata.mensaje = mensaje.mensaje
        pata.save()

        return redirect('validar')



