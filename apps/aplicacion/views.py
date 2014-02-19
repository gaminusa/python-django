# -*- coding: utf-8 -*-
from django.contrib.formtools.wizard.views import CookieWizardView
from django.shortcuts import redirect
from django.template import response
from aplicacion.models import Inscrito, PromocionesInscritos
from django.views.generic import TemplateView, View, FormView
from django.http import HttpResponse
from aplicacion.forms import DocumentoValidationForm, NuevoRegistroForm, RegistroPataForm, MensajePata
from django.conf import settings
from ubigeo.models import Ubigeo
import json


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
            tipo_doc=tipo_doc, num_doc=num_doc).exists()

        # si existe
        if value:
            #primero verifica si esta en la prmocion
            promo = PromocionesInscritos.objects.filter(dni=num_doc, id_promocion=settings.PROMOTION_ID)
            if promo:
                return redirect('gracias')
            else:
                return redirect('pata')
        # si no
        else:
            return redirect('registro')


class RegistraProcesoWizardView(CookieWizardView):
    form_list = [NuevoRegistroForm, RegistroPataForm, MensajePata]

    def get_context_data(self, form, **kwargs):
        context = super(RegistraProcesoWizardView, self).get_context_data(form, **kwargs)
        if self.steps.step0 == 0:
            context['departments'] = Ubigeo.objects.departments().using(
                'default')
        if self.steps.step0 == 1:
            context['provincias'] = Ubigeo.objects.filter(parent__pk__in=[15, 7])

        return context

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
        #import pdb; pdb.set_trace()
        nuevo = nuevo_registro.save()
        pata = registro_pata.save(commit=False)
        pata.dni_inscrito = nuevo.num_doc
        pata.save()
        pro_inscr = PromocionesInscritos(dni=nuevo.num_doc, id_promocion=settings.PROMOTION_ID)
        pro_inscr.save()
        mensaje = mensaje_pata.save(commit=False)
        pata.mensaje = mensaje.mensaje
        pata.save()
        return redirect('validar')


class GraciasView(TemplateView):
    template_name = 'pilsen/gracias.html'


class GetUbigeoView(View):
    def post(self, request, *args, **kwargs):
        response = {}
        body = json.loads(request.body)
        departa = body['departamento']
        #import pdb; pdb.set_trace()
        result = ''
        for entry in Ubigeo.objects.filter(parent=departa):
            result += '<option value="%s" %s> %s</option>' % \
                      (entry.pk, 'selected'
                      if entry.pk == departa else '', entry.name)

            response['provincia'] = result

        return HttpResponse(
            content=json.dumps(response),
            content_type='application/json'
        )


class GetDistritoView(View):
    def post(self, request, *args, **kwargs):
        response = {}
        body = json.loads(request.body)
        provincia = body['provincia']
        result = ''

        for entry in Ubigeo.objects.filter(parent=provincia):
            result += '<option value="%s" %s> %s</option>' % \
                      (entry.pk, 'selected'
                      if entry.pk == provincia else '', entry.name)

        response['provincia'] = result
        return HttpResponse(
            content=json.dumps(response),
            content_type='application/json'
        )







