import funcionesxml
import generacionpaginas
import os

def main():
 os.system("rm -r -f servicios_stic/templates/web/")
 os.system("mkdir servicios_stic/templates/web/")
 funcionesxml.inicializacion()
 generacionpaginas.generahtmlmenu()
 generacionpaginas.generaurls()
 generacionpaginas.generahtmlindex()
 generacionpaginas.generaviews()
 generacionpaginas.generaplantillas()


main()
