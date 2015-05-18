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
 nagstr = ""
 funcionesxml.inicializacion()
  
 
 for i in funcionesxml.SondaArray: 
  fichero = open("./confgSonda/host/" + generacionpaginas.formatstring(i[3][0]) + ".cfg","w")
  nagstr += "## services/" + generacionpaginas.formatstring(i[3][0]) + ".cfg \n\n"
  for j in funcionesxml.getGroupServices(funcionesxml.getGroupID(i[4])):
   ServicioSonda.append(funcionesxml.getBusinessServiceName(j))
   #print "Servicio: "+ str(funcionesxml.getBusinessServiceName(j)) + " PUERTO: " + str(funcionesxml.getPuerto(j))+ " PROTOCOLO: " + str(funcionesxml.getProtocolo(j))+ " URL: " +str(funcionesxml.getURL(j))
 
  for i in ServicioSonda:
   nagstr += "define service{\n use: "
   nagstr += i + "\n"
   nagstr += "}\n\n"
  
  
  fichero.write(nagstr)
  fichero.close
 
 
GeneraNagios()
















