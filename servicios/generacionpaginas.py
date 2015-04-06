#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#    Copyright 2014-2015
#
#      STIC - Universidad de La Laguna (ULL) <gesinv@ull.edu.es>
#
#    This file is part of Modelado de Servicios TIC.
#
#    Modelado de Servicios TIC is free software: you can redistribute it and/or modify it under
#    the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Modelado de Servicios TIC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Modelado de Servicios TIC.  If not, see
#    <http://www.gnu.org/licenses/>.
#

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
 
# Funcion para generar URLs locales
def localURLS(htmlstring):
 for i in funcionesxml.GroupArray:
  htmlstring = htmlstring.replace("\"/"+ formatstring(i[1]) + "/\"", "\"./"+ formatstring(i[1]) + ".html\"") 
 for i in funcionesxml.BusinessRoleArray:
  htmlstring = htmlstring.replace("\"/"+ formatstring(i[1]) + "/\"", "\"./"+ formatstring(i[1]) + ".html\"") 
 for i in funcionesxml.BusinessServiceArray:
  htmlstring = htmlstring.replace("\"/"+ formatstring(i[1]) + "/\"", "\"./"+ formatstring(i[1]) + ".html\"") 
 for i in funcionesxml.GroupCriticArray:
  htmlstring = htmlstring.replace("\"/"+ formatstring(i[1]) + "/\"", "\"./"+ formatstring(i[1]) + ".html\"") 
 for i in funcionesxml.BusinessServiceArray:
  htmlstring = htmlstring.replace("\"/"+ formatstring(i[1]) + "/\"", "\"./"+ formatstring(i[1]) + ".html\"") 
 return htmlstring


# Generacion de fichero HTML para grupo de servicios, de criticidad o por roles
def generahtmlgrupo(nombreGrupo,nombreuni="",nombrecorto=""):
  formatstring(nombreGrupo)
  if (nombrecorto != ""):
   nombrecorto+="/templates/"
  fichero = open("servicios_stic/templates/" + nombrecorto + formatstring(nombreGrupo) + ".html","w")
  if(nombrecorto == ""):
   htmlstr = """ 
{% extends "menu.html" %}"""
  else:
   htmlstr = """ 
{% extends "menu2.html" %}"""
  htmlstr+= """

{% block contenido %}
{% block titulo %}
	<li class="active">""" + nombreuni + """ - <a href="{% url "servicios_stic.views.index"%}">Carta de Servicios del STIC</a> - """ + nombreGrupo + """</li>
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
  if(nombrecorto != ""):
   from django.template.loader import render_to_string  
   rendered = render_to_string(""+ nombrecorto + formatstring(nombreGrupo) + ".html")
   rendered = localURLS(rendered)
   fichero = open("servicios_stic/templates/" + nombrecorto + formatstring(nombreGrupo) + ".html","w") 
   fichero.write(rendered)
   fichero.close()

# Generacion de fichero HTML para cada Servicio
def generahtmlservicio(serviceID,nombreuni="",nombrecorto=""):
  nombreServicio = funcionesxml.getBusinessServiceName(serviceID)
  if (nombrecorto != ""):
   nombrecorto+="/templates/"
  fichero = open("servicios_stic/templates/" + nombrecorto + formatstring(nombreServicio) + ".html","w")
  if (nombrecorto == ""):
   htmlstr = """ 
{% extends "menu.html" %}"""
  else:
   htmlstr = """ 
{% extends "menu2.html" %}"""
  htmlstr+= """	  
{% block contenido %}
{% block titulo %}
																																    
	<li class="active">""" + nombreuni + """ - <a href="{% url "servicios_stic.views.index"%}">Carta de Servicios del STIC</a> - <a href="{% url "servicios_stic.views."""+ formatstring(funcionesxml.getServiceGroup(serviceID)) + """" %}"> """ + str(funcionesxml.getServiceGroup(serviceID)) + """</a> - """+ nombreServicio + """</li>
{% endblock %}

{% block content %}
	<div class="container-fluid">
		<div class="row">
			<div class="col-md-9 col-md-push-3" role="main"> 
				<br><br>
					<h1 class="main-title">""" + nombreServicio + """</h1>
					<p> ID: """ + serviceID + """ </p>
					<p> Grupo de Servicio: """ + str(funcionesxml.getServiceGroup(serviceID)) + """ </p>
					<p> Criticidad: """+ str(funcionesxml.getServiceCritic(serviceID)) +"""</p>
					<p> Nivel de Acceso: """+ str(funcionesxml.getServiceAccess(serviceID)) +"""</p>
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
  if(nombrecorto != ""):
   from django.template.loader import render_to_string  	  
   rendered = render_to_string(""+ nombrecorto + formatstring(nombreServicio) + ".html")
   rendered = localURLS(rendered)
   fichero = open("servicios_stic/templates/" + nombrecorto + formatstring(nombreServicio) + ".html","w") 
   fichero.write(rendered)
   fichero.close()
   
# Generación de fichero html para menú lateral
def generahtmlmenu(nombrecorto=""):
  if (nombrecorto != ""):
   nombrecorto+="/templates/"
  fichero = open("servicios_stic/templates/" + nombrecorto + "menu.html","w")
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
  if(nombrecorto != ""):
    fichero = open("servicios_stic/templates/menu2.html","w")  
    fichero.write(httmlstr)
    fichero.close()

# Generación del fichero Views.py  
def generaviews():
  
  fichero = open("servicios_stic/views.py","w")

  pystr = """
from django.shortcuts import render_to_response
from servicios_stic.forms import UploadForm
from servicios_stic.models import Document
from django.shortcuts import render, redirect
from django.http import HttpResponse

import main
import os 
import zipfile

def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save(form)
            newimg = Document(imagefile = request.FILES['imagefile'])
            newimg.save(form)
            nombreuni = request.POST.get('Nombre_Universidad')
            nombrecorto = request.POST.get('Nombre_Universidad_Corto')
            main.main(nombreuni,nombrecorto)
            zf = zipfile.ZipFile((""+ str(nombrecorto) + ".zip"), "w")
            for dirname, subdirs, files in os.walk("servicios_stic/templates/"+ nombrecorto):
              zf.write(dirname)
              for filename in files:
               zf.write(os.path.join(dirname, filename))
            zf.close()

            response = HttpResponse(open(""+nombrecorto+".zip").read(),content_type="application/zip")  
            response["Content-Disposition"] = "attachment; filename="+ nombrecorto +".zip"  
            return response
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form}) 
    
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
 url(r'^uploads/', 'servicios_stic.views.upload_file', name="uploads"), 
 url(r'^admin/', include(admin.site.urls)),

)
"""
  pystr += pystrii
  fichero.write(pystr)
  fichero.close()

# Generacion del fichero index.html
def generahtmlindex(nombreuni="",nombrecorto=""):
  if (nombrecorto != ""):
   nombrecorto+="/templates/"
  fichero = open("servicios_stic/templates/" + nombrecorto + "index.html","w")
  httmlstr = """{% extends "plantilla.html" %}

{% block contenido %}
{% block titulo %}
	<li class="active">""" + nombreuni + """ - Carta de Servicios del STIC</li>
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
  if(nombrecorto != ""):
   from django.template.loader import render_to_string  
   rendered = render_to_string(""+ nombrecorto +"index.html")
   rendered = localURLS(rendered)
   fichero = open("servicios_stic/templates/" + nombrecorto + "index.html","w") 
   fichero.write(rendered)
   fichero.close()

# Generación de todos los ficheros necesarios
def generaplantillas(nombreuni="",nombrecorto=""):   
  for i in funcionesxml.GroupArray:
   generahtmlgrupo(str(i[1]),nombreuni,nombrecorto)
  for j in funcionesxml.GroupCriticArray:		 
   generahtmlgrupo(str(j[1]),nombreuni,nombrecorto)
  for k in funcionesxml.GroupRoleArray:		 
   generahtmlgrupo(str(k[1]),nombreuni,nombrecorto)
  for l in funcionesxml.BusinessServiceArray:
   generahtmlservicio(str(l[0]),nombreuni,nombrecorto)




