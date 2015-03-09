
from django.conf.urls import patterns, include, url
from django.contrib import admin
from servicios_stic.views import *

urlpatterns = patterns('',
 url(r'^$', 'servicios_stic.views.index', name='index'),
	
 url(r'^soporte_tic_a_la_investigacion/$', 'servicios_stic.views.soporte_tic_a_la_investigacion', name='soporte_tic_a_la_investigacion'),	
 url(r'^soporte_tic_a_la_docencia/$', 'servicios_stic.views.soporte_tic_a_la_docencia', name='soporte_tic_a_la_docencia'),	
 url(r'^soporte_tic_a_la_gestion/$', 'servicios_stic.views.soporte_tic_a_la_gestion', name='soporte_tic_a_la_gestion'),	
 url(r'^servicios_criticos/$', 'servicios_stic.views.servicios_criticos', name='servicios_criticos'),	
 url(r'^servicios_normales/$', 'servicios_stic.views.servicios_normales', name='servicios_normales'),	
 url(r'^servicios_poco_criticos/$', 'servicios_stic.views.servicios_poco_criticos', name='servicios_poco_criticos'),	
 url(r'^alumnos/$', 'servicios_stic.views.alumnos', name='alumnos'),	
 url(r'^pas/$', 'servicios_stic.views.pas', name='pas'),	
 url(r'^pdi/$', 'servicios_stic.views.pdi', name='pdi'),	
 url(r'^exalumnos/$', 'servicios_stic.views.exalumnos', name='exalumnos'),	
 url(r'^aaaaull/$', 'servicios_stic.views.aaaaull', name='aaaaull'),
 url(r'^admin/', include(admin.site.urls)),

)
