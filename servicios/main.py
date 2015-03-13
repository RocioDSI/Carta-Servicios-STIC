import funcionesxml
import generacionpaginas
import os

def main(newstr=""):
	
 if(newstr==""): 
  newstr = "Universidad de La Laguna"
 os.system("rm -r -f servicios_stic/templates/web/")
 os.system("mkdir servicios_stic/templates/web/")
 funcionesxml.inicializacion()
 generacionpaginas.generahtmlmenu()
 generacionpaginas.generaurls()
 generacionpaginas.generahtmlindex(newstr)
 generacionpaginas.generaviews()
 generacionpaginas.generaplantillas(newstr)


