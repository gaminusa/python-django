from django.conf import settings
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^index/', include('aplicacion.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    from django.views.static import serve
    urlpatterns += patterns(
        '',
        url(r'^media/(?P<path>.*)$',
            serve, {
            'document_root': settings.MEDIA_ROOT,
            'show_indexes': True}),
        url(r'^static/(?P<path>.*)$',
            serve, {
            'document_root': settings.STATIC_ROOT,
            'show_indexes': True}),
    )