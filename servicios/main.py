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


