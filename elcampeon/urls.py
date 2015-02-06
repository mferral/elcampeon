from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'elcampeon.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'app.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^acceso/', 'app.views.login', name='login'),
    url(r'^frmnota/$', 'app.views.frmnota', name='frmnota'),
    url(r'^frmpublicidad/$', 'app.views.frmpublicidad', name='frmpublicidad'),
    url(r'^validar/', 'app.views.validar', name='validar'),
    url(r'^noticias/', 'app.views.noticias', name='noticias'),
    url(r'^otras_secciones/(?P<idseccion>\d+)/$','app.views.otras_secciones'),
    url(r'^noticias_principal/(?P<idpagina>\d+)','app.views.noticias_principal'),
    url(r'^seccion_noticias/(?P<idseccion>\d+)/(?P<idpagina>\d+)','app.views.secciones_pagina'),  
    url(r'^noticia_save/', 'app.views.noticia_save'),
    url(r'^publicidad_save/', 'app.views.publicidad_save'),
    url(r'^publicidad_delete/', 'app.views.publicidad_delete'),
    url(r'^noticia_delete/', 'app.views.noticia_delete'),
    url(r'^tabla_noticias/(?P<palabra>.*)', 'app.views.tabla_noticias'),    
    url(r'^tabla_publicidad/', 'app.views.tabla_publicidad'),    
    url(r'^seccion/(?P<idseccion>\d+)', 'app.views.seccion'),
    url(r'^entrada/(?P<identrada>\d+)', 'app.views.entrada'),

    url(r'^publicidad/', 'app.views.publicidad', name='publicidad'),

    url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
    }),
)
