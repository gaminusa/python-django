# -*- coding: utf-8 -*-

from django.conf.urls import patterns, include, url
from aplicacion import views

urlpatterns = patterns('',
    url(r'^validar/$', views.ValidarView.as_view(), name='validar'),
    url(r'^registro/$', views.RegistroNuevoView.as_view(), name='registro'),
    url(r'^$', views.IndexView.as_view(), name='index'),
)

