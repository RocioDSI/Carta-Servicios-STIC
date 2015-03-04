
from django.conf.urls import patterns, include, url
from django.contrib import admin
from servicios_stic.views import *

urlpatterns = patterns('',
 url(r'^$', 'servicios_stic.views.index', name='index'),
	
 url(r'^soporte_tic_a_la_investigacion/$', 'servicios_stic.views.soporte_tic_a_la_investigacion', name='soporte_tic_a_la_investigacion'),	
 url(r'^soporte_tic_a_la_docencia/$', 'servicios_stic.views.soporte_tic_a_la_docencia', name='soporte_tic_a_la_docencia'),	
 url(r'^soporte_tic_a_la_gestion/$', 'servicios_stic.views.soporte_tic_a_la_gestion', name='soporte_tic_a_la_gestion'),
 url(r'^admin/', include(admin.site.urls)),

)
