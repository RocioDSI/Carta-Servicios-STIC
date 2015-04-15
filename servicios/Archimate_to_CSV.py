#!/usr/bin/python
# -*- coding: utf-8 -*-

import funcionesxml


lista = funcionesxml.nodos[0].getElementsByTagName("folder")
listaEl = funcionesxml.nodos[0].getElementsByTagName("element")
listaFinal = []
ArrayRediris = []

def main():
 funcionesxml.inicializacion()
	
 #f = open('datos.csv','w')
 
 #for i in funcionesxml.BusinessServiceArray:
  #f.write(str(i[0]))
  #f.write('\n')
 
  #for i in lista:
 nombre_servicios=[]
 
#SELECCIÓN DE SERVICIOS ACCESIBLES DESDE INTERNET CON CRITICIDAD ALTA 
 for aux in funcionesxml.BusinessServiceArray:	 
  if(aux[4] == "Alta") and (aux[5] == "Internet"):
  # print("Nombre: " + aux[1] + ".\tCriticidad: " + str(aux[4]) + ".\tNivel de acceso: " + str(aux[5]))
   ArrayRediris.append(str(aux[1]))
   
#SELECCIÓN DE NOMBRES DE 
 for i in lista:
  if(i.attributes.get("name").value == "Application"):  
   for j in listaEl:
    if(j.attributes.get("xsi:type").value  == "archimate:ApplicationService"):
     list_prop = j.getElementsByTagName("property")
     nombre_servicios.append(j.attributes.get("name").value)
     for k in list_prop:
      clave = []
      valor = []
      valoriris = []
      claveiris = []
      if(k.attributes.get("value") != None):
       valor.append(k.attributes.get("value").value) 
      else:
       valor.append("Campo Vacío")
      if (k.attributes.get("key").value == "URL_Servicio"):
       claveiris.append(k.attributes.get("key").value)  
       valoriris.append(k.attributes.get("value").value)
      if (k.attributes.get("key").value == "Puerto_Servicio"):  
       claveiris.append(k.attributes.get("key").value)  
       valoriris.append(k.attributes.get("value").value)
      listaFinal.append(claveiris)
      listaFinal.append(valoriris)
      print listaFinal
     
 #for i in ArrayRediris:
  #print str(i)
  
 #print listaFinal
  
  
main()
	
	
	



