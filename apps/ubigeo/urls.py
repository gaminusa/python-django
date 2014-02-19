# -*- coding: utf-8 -*-

from django.conf.urls import patterns, url


urlpatterns = patterns('ubigeo.views',
        #url(r'^get_ubigeo/<ubigeo_id:#>/', 'get_ubigeo', name='get_ubigeo'),
        #url(r'^ubigeo/$', 'widget', name='widget'),
        url('^department/$', 'get_deparments'),
        url('^province/(?P<department>\d+)/$', 'get_provinces'),
        url('^district/(?P<province>\d+)/$', 'get_districts'),
        #url('^check_validate_email/(?P<email>\w+)/$', 'main.views.check_validate_email'),
)
