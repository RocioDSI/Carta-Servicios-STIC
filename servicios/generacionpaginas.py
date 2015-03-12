#!/usr/bin/python
# -*- coding: utf-8 -*-

import funcionesxml
import os 

# Funcion para eliminar caracteres extraños de strings
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
  nombrProc=nombrProc.replace("ñ","n")
  nombrProc=nombrProc.replace("ç","c")
  nombrProc=nombrProc.replace("-","_")
  nombrProc=nombrProc.replace(" ","_")
  nombrProc=nombrProc.replace("(","_")
  nombrProc=nombrProc.replace(")","_")
  nombrProc=nombrProc.replace("&","_")
  nombrProc=nombrProc.replace("/","_")
  nombrProc=nombrProc.replace("%","_")
  nombrProc=nombrProc.replace(".","")
  nombrProc=nombrProc.lower()
  return nombrProc

# Generacion de fichero HTML para grupo de servicios, de criticidad o por roles
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
                    <li class="active"><a href="{% url "servicios_stic.views.""" + formatstring(funcionesxml.getBusinessServiceName(str(i))) + """" %}"><h1 class="main-title">""" + funcionesxml.getBusinessServiceName(str(i)) + """</h1></a></li>
                    <p> Roles: """  
   htmlstr += htmlstrii
   k = 0
   for j in funcionesxml.getServiceRoles(i):
    if (k < len(funcionesxml.getServiceRoles(i))-1):
     htmlroles = """""" + str(funcionesxml.getGroupName(j)) + """, """   
     htmlstr += htmlroles
     k +=1
    else:
     htmlroles = """""" + str(funcionesxml.getGroupName(j)) + """. """   
     htmlstr += htmlroles
     
   htmlstr += """</p>
   """	  
   for k in range(0, len(funcionesxml.getServiceProperties(i)[0])):
      if(str((funcionesxml.getServiceProperties(i)[0][k])) == "Descripción"):
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

# Generacion de fichero HTML para cada Servicio
def generahtmlservicio(serviceID):
  nombreServicio = funcionesxml.getBusinessServiceName(serviceID)
  fichero = open("servicios_stic/templates/" + formatstring(nombreServicio) + ".html","w")
  htmlstr = """ 
{% extends "menu.html" %}

{% block contenido %}
{% block titulo %}
																																    
	<li class="active">Universidad de La Laguna - <a href="{% url "servicios_stic.views.index"%}">Carta de Servicios del STIC</a> - <a href="{% url "servicios_stic.views."""+ formatstring(funcionesxml.getServiceGroup(serviceID)) + """" %}"> """ + str(funcionesxml.getServiceGroup(serviceID)) + """</a> - """+ nombreServicio + """</li>
{% endblock %}

{% block content %}
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-9 col-md-push-3" role="main"> 
				<br><br>
					<h1 class="main-title">""" + nombreServicio + """</h1>
					<p> ID: """ + serviceID + """ </p>
					<p> Grupo de Servicio: """ + str(funcionesxml.getServiceGroup(serviceID)) + """ </p>
					<p> Criticidad: """+ str(funcionesxml.ServiceCritic(serviceID)) +"""</p>
                    <p> Roles: """  
		 
  
  k = 0
  for j in funcionesxml.getServiceRoles(serviceID):
   if (k < len(funcionesxml.getServiceRoles(serviceID))-1):
    htmlroles = """""" + str(funcionesxml.getGroupName(j)) + """, """   
    htmlstr += htmlroles
    k +=1
   else:
    htmlroles = """""" + str(funcionesxml.getGroupName(j)) + """. """   
    htmlstr += htmlroles
     
  htmlstr += """</p>
   """	  
  for k in range(0, len(funcionesxml.getServiceProperties(serviceID)[0])):
      htmliii= """<p> """ + str((funcionesxml.getServiceProperties(serviceID)[0][k])) + """: """ + str((funcionesxml.getServiceProperties(serviceID)[1][k])) + """ </p>
      """
      htmlstr += htmliii

  htmlstriv= """		</div>
{% endblock %}
{% endblock %}  
  """	
  htmlstr += htmlstriv
  fichero.write(htmlstr)
  fichero.close()

# Generación de fichero html para menú lateral
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

{% block menucritic %}
                       <div class="panel panel-default panel-ull color-336699">
                            <div class="panel-heading">
                                <h3 class="panel-title"><i class="fa fa-file"></i> Grupos de Criticidad</h3>
                            </div>
                            <div class="panel-body">
                                <ul class="nav nav-pills nav-stacked">
"""
  httmlstr += htmlstrii
  for i in funcionesxml.GroupCriticArray:
   grupostring = """                                 <li><a href="{% url "servicios_stic.views.""" + formatstring(str(i[1])) + """" %}">""" + str(i[1])+ """</a></li>
"""
   httmlstr+=grupostring 
  htmlstrii = """                                </ul>
                            </div>
                        </div>
{%endblock%}

{% block menurole %}
                       <div class="panel panel-default panel-ull color-336699">
                            <div class="panel-heading">
                                <h3 class="panel-title"><i class="fa fa-file"></i> Roles</h3>
                            </div>
                            <div class="panel-body">
                                <ul class="nav nav-pills nav-stacked">
"""
  httmlstr += htmlstrii
  for i in funcionesxml.GroupRoleArray:
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


# Generación del fichero Views.py  
def generaviews():
  
  fichero = open("servicios_stic/views.py","w")

  pystr = """
from django.shortcuts import render_to_response
import funcionesxml

def index(request):
 response = render_to_response('index.html')
 return response
  """
  
  for i in funcionesxml.GroupArray:
	 viewgrupo = """
def """ + formatstring(str(i[1])) + """(request):
 response = render_to_response('""" + formatstring(str(i[1]))+ """.html')
 return response
	   
	   """
	 pystr += viewgrupo
	 
  for i in funcionesxml.GroupCriticArray:
     viewgrupo = """
def """ + formatstring(str(i[1])) + """(request):
 response = render_to_response('""" + formatstring(str(i[1]))+ """.html')
 return response
	   
	   """
     pystr += viewgrupo

  for i in funcionesxml.GroupRoleArray:
     viewgrupo = """
def """ + formatstring(str(i[1])) + """(request):
 response = render_to_response('""" + formatstring(str(i[1]))+ """.html')
 return response
	   
	   """
     pystr += viewgrupo
     
  for i in funcionesxml.BusinessServiceArray:
	 viewservice = """
def """ + formatstring(str(i[1])) + """(request):
 response = render_to_response('""" + formatstring(str(i[1]))+ """.html')
 return response
	   
	   """
	 pystr += viewservice
	 
  fichero.write(pystr)
  fichero.close()

# Generacion del fichero urls.py
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
  for i in funcionesxml.GroupCriticArray:
   urlgrupo = """	
 url(r'^""" + formatstring(str(i[1])) + """/$', 'servicios_stic.views.""" + formatstring(str(i[1])) + """', name='"""+ formatstring(str(i[1])) + """'),"""  
   pystr+= urlgrupo
  for i in funcionesxml.GroupRoleArray:
   urlgrupo = """	
 url(r'^""" + formatstring(str(i[1])) + """/$', 'servicios_stic.views.""" + formatstring(str(i[1])) + """', name='"""+ formatstring(str(i[1])) + """'),"""  
   pystr+= urlgrupo
  for i in funcionesxml.BusinessServiceArray:
   urlservice = """	
 url(r'^""" + formatstring(str(i[1])) + """/$', 'servicios_stic.views.""" + formatstring(str(i[1])) + """', name='"""+ formatstring(str(i[1])) + """'),"""  
   pystr+= urlservice

  pystrii = """
 url(r'^admin/', include(admin.site.urls)),

)
"""
  pystr += pystrii
  fichero.write(pystr)
  fichero.close()

# Generacion del fichero index.html
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

# Generación de todos los ficheros necesarios
def generaplantillas():
  for i in funcionesxml.GroupArray:
   generahtmlgrupo(str(i[1]))
  for j in funcionesxml.GroupCriticArray:		 
   generahtmlgrupo(str(j[1]))
  for k in funcionesxml.GroupRoleArray:		 
   generahtmlgrupo(str(k[1]))
  for l in funcionesxml.BusinessServiceArray:
   generahtmlservicio(str(l[0]))




