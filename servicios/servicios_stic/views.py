
from django.shortcuts import render_to_response
import funcionesxml

def index(request):
 funcionesxml.inicializacion()
 name = []
 for i in funcionesxml.GroupArray:
  name.append(str(i[1]))
 response = render_to_response('index.html',{'grupo': name })
 return response
  
def soporte_tic_a_la_investigacion(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("fd5a95c7")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('soporte_tic_a_la_investigacion.html',{'servicio': name })
 return response
	   
	   
def soporte_tic_a_la_docencia(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("e589b1c3")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('soporte_tic_a_la_docencia.html',{'servicio': name })
 return response
	   
	   
def soporte_tic_a_la_gestion(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("2ce262c7")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('soporte_tic_a_la_gestion.html',{'servicio': name })
 return response
	   
	   