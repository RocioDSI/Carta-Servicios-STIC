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

funcionesxml.inicializacion()
listaEl = funcionesxml.nodos[0].getElementsByTagName("element")

def sonda_to_csv():
   for i in funcionesxml.SondaArray:
    csvstr = ""
    fichero = open("./Sondas_CSV/" + generacionpaginas.formatstring(i[3][0]) + ".csv","w")
    csvstr += str(i[2][0]) + ": " + str(i[3][0])  + ", " + str(i[2][1])+ ": " + str(i[3][1]) + ", " + str(i[2][2])+ ": " + str(i[3][2]) + "," + str(i[4]) + ", \n \n"  
    csvstr += "Servicio, Enlace, Puerto, Protocolo, Nivel de Acceso \n"     
    
    for q in funcionesxml.GroupAccessArray:
     if(funcionesxml.getNivelAcceso(q[0]) <= funcionesxml.getNivelAcceso(funcionesxml.getGroupID(i[4]))):		
      for j in funcionesxml.getGroupServices(q[0]):
       csvstr += funcionesxml.getBusinessServiceName(j) +", "
       app_ok = 0          
       for k in listaEl:
        if(k.attributes.get("xsi:type").value  == "archimate:ApplicationService"):
         if(str(funcionesxml.getBusinessServiceName(j)) == str(funcionesxml.getUsedByBusiness(k.attributes.get("id").value))):
          app_ok = 1
          list_prop = k.getElementsByTagName("property")
          for k in list_prop:
           if(k.attributes.get("value") != None):
             csvstr += (k.attributes.get("value").value) +", "
           else:
            csvstr += "Campo Vacío, "
       if app_ok == 0:
        csvstr += " None ,  None ,  None ,"        
       csvstr += q[1] + ", \n"
    fichero.write(csvstr)
    fichero.close
	
	
	
sonda_to_csv()
