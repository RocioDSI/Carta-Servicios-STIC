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
import generacionpaginas

ServicioSonda = [] #Vector que contendrá los servicios de una sonda

#Creacion fichero configuracion Nagios
def GeneraNagios():
 nagstr1 = ""
 nagstr2 = ""
 nagstr3 = ""
 
 funcionesxml.inicializacion()
  
 
 for i in funcionesxml.SondaArray: 
  #CREACION DE FICHEROS NAGIOS
  ficheroservicio = open("./confgSonda/servicio/" + generacionpaginas.formatstring(i[3][0]) + ".cfg","w")
  ficherohost = open("./confgSonda/host/" + generacionpaginas.formatstring(i[3][0]) + ".cfg","w")
  ficherohost_group = open("./confgSonda/host_group/" + generacionpaginas.formatstring(i[3][0]) + ".cfg","w")
  
  #CREACION FICHEROS SERVICIO
  nagstr1 += "## services/" + generacionpaginas.formatstring(i[3][0]) + ".cfg \n\n"
  for j in funcionesxml.getGroupServices(funcionesxml.getGroupID(i[4])):
   ServicioSonda.append(funcionesxml.getBusinessServiceName(j))
   #print "Servicio: "+ str(funcionesxml.getBusinessServiceName(j)) + " PUERTO: " + str(funcionesxml.getPuerto(j))+ " PROTOCOLO: " + str(funcionesxml.getProtocolo(j))+ " URL: " +str(funcionesxml.getURL(j))
  for k in ServicioSonda:
   nagstr1 += "define service{\n use: "
   nagstr1 += k + "\n" + " host_name: " + "---\n" + " contact_groups: " + "---\n"
   nagstr1 += "}\n\n"
  
  #CREACION FICHEROS HOST_GROUP
  nagstr2 += "## host_group/" + generacionpaginas.formatstring(i[3][0]) + ".cfg \n\n"
  nagstr2 += "define hostgroup{\n hostgroup_name: " + "---\n " + "alias: " + "---\n " + "members: " + "---\n"
  nagstr2 += "}\n\n"
   
   
  #CREACION FICHEROS HOST_GROUP
  nagstr3 += "## host/" + generacionpaginas.formatstring(i[3][0]) + ".cfg \n\n"
  nagstr3 += " "

  
  ficheroservicio.write(nagstr1)
  ficherohost.write(nagstr3)
  ficherohost_group.write(nagstr2)
  ficheroservicio.close
  ficherohost.close
  ficherohost_group.close
 
 
GeneraNagios()
















