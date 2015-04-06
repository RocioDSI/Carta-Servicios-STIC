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
import os
import shutil

def main(nombreuni="", nombrecorto=""):
	
 if(nombreuni==""): 
  nombreuni = "Universidad de La Laguna"
 
 if (nombrecorto != ""):
  print "Creando directorios"
  os.system("mkdir servicios_stic/templates/"+ str(nombrecorto))
  os.system("mkdir servicios_stic/templates/"+ str(nombrecorto) + "/templates/")
  os.system("mkdir servicios_stic/templates/"+ str(nombrecorto) + "/css/")
  shutil.copyfile("servicios_stic/css/Logo.jpg", "servicios_stic/templates/"+ str(nombrecorto)+"/css/Logo.jpg")
  shutil.copyfile("servicios_stic/css/estilos.css", "servicios_stic/templates/"+ str(nombrecorto)+"/css/estilos.css")
  shutil.copyfile("servicios_stic/templates/plantilla.html", "servicios_stic/templates/"+ str(nombrecorto) +"/templates/plantilla.html")
 
 os.system("rm -r -f servicios_stic/templates/web/")
 os.system("mkdir servicios_stic/templates/web/")
 funcionesxml.inicializacion()
 generacionpaginas.generahtmlmenu(nombrecorto)
 generacionpaginas.generaurls()
 generacionpaginas.generahtmlindex(nombreuni,nombrecorto)
 generacionpaginas.generaviews()
 generacionpaginas.generaplantillas(nombreuni,nombrecorto)


