# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from aplicacion import views

urlpatterns = patterns('',
    url(r'^validar/$', views.ValidarView.as_view(), name='validar'),
    url(r'^gracias/$', views.GraciasView.as_view(), name='gracias'),
    url(r'^ubigeo/$', views.GetUbigeoView.as_view(), name='ubigeo'),
    url(r'^distrito/$', views.GetDistritoView.as_view(), name='distrito'),
    url(r'^registro/$', views.RegistraProcesoWizardView.as_view(), name='registro'),
    url(r'^$', views.IndexView.as_view(), name='index'),
)

