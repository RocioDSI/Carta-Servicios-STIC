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

lista = funcionesxml.nodos[0].getElementsByTagName("folder")
listaEl = funcionesxml.nodos[0].getElementsByTagName("element")
listaFinal = []
ArrayRediris = []

def main():
 funcionesxml.inicializacion()
 LecturaPuertosValores()
 
def LecturaPuertosValores():
	
 nombre_servicios=[]
 
 #SELECCIÓN DE SERVICIOS ACCESIBLES DESDE INTERNET CON CRITICIDAD ALTA 
 for aux in funcionesxml.BusinessServiceArray:	 
  if(aux[4] == "Alta") and (aux[5] == "Internet"):
   ArrayRediris.append(str(aux[1]))

  
 for j in listaEl:
  if(j.attributes.get("xsi:type").value  == "archimate:ApplicationService"):
   servicio = funcionesxml.getUsedByBusiness(j.attributes.get("id").value)
   list_prop = j.getElementsByTagName("property")
   nombre_servicios.append(j.attributes.get("name").value)
   for k in list_prop:
    valor = []
    if(k.attributes.get("value") != None):
     valor.append(k.attributes.get("value").value) 
    else:
     valor.append("Campo Vacío")
    if (k.attributes.get("key").value == "URL_Servicio") or (k.attributes.get("key").value == "Puerto_Servicio") or (k.attributes.get("key").value == "Protocolo_Servicio"):
     claveiris = str(k.attributes.get("key").value)  
     valoriris = (str(k.attributes.get("value").value))
    if servicio in ArrayRediris:
     if servicio not in listaFinal:		
       listaFinal.append(str(servicio))
     listaFinal.append(str(valoriris))
 
 
 cont = 0
 csvstr = "Servicio, Enlace, Puerto, Protocolo \n"
 for i in listaFinal:
  csvstr = csvstr + i + ", "
  cont = cont + 1
  if cont == 4:
   cont = 0
   csvstr = csvstr + "\n"
   
 f = open("out.csv","w")
 f.write(csvstr)
 f.close()
 print csvstr
main()
	
	
	



