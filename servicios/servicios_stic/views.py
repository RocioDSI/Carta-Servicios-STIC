
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
 servicios = funcionesxml.getGroupServices("68821cb1")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('soporte_tic_a_la_gestion.html',{'servicio': name })
 return response
	   
	   
def servicios_criticos(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("2810a262")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('servicios_criticos.html',{'servicio': name })
 return response
	   
	   
def servicios_normales(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("94f5f712")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('servicios_normales.html',{'servicio': name })
 return response
	   
	   
def servicios_poco_criticos(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("23956b5a")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('servicios_poco_criticos.html',{'servicio': name })
 return response
	   
	   
def alumnos(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("8e132732")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('alumnos.html',{'servicio': name })
 return response
	   
	   
def pas(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("ab9ab0df")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('pas.html',{'servicio': name })
 return response
	   
	   
def pdi(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("0159aabe")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('pdi.html',{'servicio': name })
 return response
	   
	   
def exalumnos(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("15e890fb")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('exalumnos.html',{'servicio': name })
 return response
	   
	   
def aaaaull(request):
 funcionesxml.inicializacion()
 name = []
 servicios = funcionesxml.getGroupServices("ad712805")
 for i in servicios:
  name.append(funcionesxml.getBusinessServiceName(i))
 response = render_to_response('aaaaull.html',{'servicio': name })
 return response
	   
	   