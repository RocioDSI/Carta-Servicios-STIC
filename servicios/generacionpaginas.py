#!/usr/bin/python
# -*- coding: utf-8 -*-

import funcionesxml


def formatstring(nombreGrupo):
  nombrProc = nombreGrupo
  nombrProc=nombrProc.replace("Á","a")
  nombrProc=nombrProc.replace("É","e")
  nombrProc=nombrProc.replace("Í","i")
  nombrProc=nombrProc.replace("Ó","o")
  nombrProc=nombrProc.replace("Ú","u")  
  nombrProc=nombrProc.replace('á','a')
  nombrProc=nombrProc.replace("é","e")
  nombrProc=nombrProc.replace("í","i")
  nombrProc=nombrProc.replace("ó","o")
  nombrProc=nombrProc.replace("ú","u")
  nombrProc=nombrProc.replace(" ","_")
  nombrProc=nombrProc.lower()
  return nombrProc
  
def generahtmlgrupo(nombreGrupo):
  formatstring(nombreGrupo)
  fichero = open("servicios_stic/templates/" + formatstring(nombreGrupo) + ".html","w")
  htmlstr = """ 
{% extends "menu.html" %}

{% block contenido %}
{% block titulo %}
	<li class="active">Universidad de La Laguna - <a href="{% url "servicios_stic.views.index"%}">Carta de Servicios del STIC</a> - """ + nombreGrupo + """</li>
{% endblock %}

{% block content %}
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-9 col-md-push-3" role="main"> 
				<br><br>"""
  for i in funcionesxml.getGroupServices(funcionesxml.getGroupID(nombreGrupo)):
   htmlstrii = """
					<h1 class="main-title">""" + funcionesxml.getBusinessServiceName(str(i)) + """</h1> 
					<p> ID: """ + i + """ </p>"""
   htmlstr += htmlstrii
 
   for k in range(0, len(funcionesxml.getServiceProperties(i)[0])):
       htmliii= """<p> """ + str((funcionesxml.getServiceProperties(i)[0][k])) + """: """ + str((funcionesxml.getServiceProperties(i)[1][k])) + """ </p>
       """
       htmlstr += htmliii

  htmlstriv= """		</div>
{% endblock %}
{% endblock %}  
  """	
  htmlstr += htmlstriv
  fichero.write(htmlstr)
  fichero.close()

def generahtmlmenu():
  fichero = open("servicios_stic/templates/menu.html","w")
  httmlstr = """{% extends "plantilla.html" %}

{% block menu %}
                       <div class="panel panel-default panel-ull color-336699">
                            <div class="panel-heading">
                                <h3 class="panel-title"><i class="fa fa-file"></i> Servicios</h3>
                            </div>
                            <div class="panel-body">
                                <ul class="nav nav-pills nav-stacked">
"""
  for i in funcionesxml.GroupArray:
   grupostring = """                                 <li><a href="{% url "servicios_stic.views.""" + formatstring(str(i[1])) + """" %}">""" + str(i[1])+ """</a></li>
"""
   httmlstr+=grupostring 
   
  htmlstrii = """                                </ul>
                            </div>
                        </div>
{%endblock%}
{%block contenido%}{%endblock%}

"""
  httmlstr+= htmlstrii
  fichero.write(httmlstr)
  fichero.close()
  
def generaviews():
  
  fichero = open("servicios_stic/views.py","w")
   
  pystr = """
from django.shortcuts import render_to_response
import funcionesxml

def index(request):
 funcionesxml.inicializacion()
 name = []
 for i in funcionesxml.GroupArray:
  name.append(str(i[1]))
 response = render_to_response('index.html',{'grupo': name })
 return response
  """
  for i in funcionesxml.GroupArray:
	 viewgrupo = """
def """ + formatstring(str(i[1])) + """(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices(\""""+ str(i[0])+"""\")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('""" + formatstring(str(i[1]))+ """.html',{'servicio': name })
 return response
	   
	   """
	 pystr += viewgrupo
	  
  fichero.write(pystr)
  fichero.close()

def generaurls():
  fichero = open("servicios/urls.py","w")
  pystr = """
from django.conf.urls import patterns, include, url
from django.contrib import admin
from servicios_stic.views import *

urlpatterns = patterns('',
 url(r'^$', 'servicios_stic.views.index', name='index'),
"""
  for i in funcionesxml.GroupArray:
   urlgrupo = """	
 url(r'^""" + formatstring(str(i[1])) + """/$', 'servicios_stic.views.""" + formatstring(str(i[1])) + """', name='"""+ formatstring(str(i[1])) + """'),"""  
   pystr+= urlgrupo
  pystrii = """
 url(r'^admin/', include(admin.site.urls)),

)
"""
  pystr += pystrii
  fichero.write(pystr)
  fichero.close()


def generahtmlindex():
  fichero = open("servicios_stic/templates/index.html","w")
  httmlstr = """{% extends "plantilla.html" %}

{% block contenido %}
{% block titulo %}
	<li class="active">Universidad de La Laguna - Carta de Servicios del STIC</li>
{% endblock %}

{% block content %}
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-9 col-md-push-3" role="main"> 
				<br><br>
"""
  for i in funcionesxml.GroupArray:
   grupostring = """				 <li class="active"><a href="{% url "servicios_stic.views.""" + formatstring(str(i[1])) + """" %}"><h1 class="main-title">""" + str(i[1]) + """</h1></a></li>
"""
   httmlstr+=grupostring 
   				
  htmlstrii ="""			</div>
{% endblock %}
{% endblock %}"""

  httmlstr+= htmlstrii
  fichero.write(httmlstr)
  fichero.close()
  

  
def generaplantillas():
  for i in funcionesxml.GroupArray:
   generahtmlgrupo(str(i[1]))		 

