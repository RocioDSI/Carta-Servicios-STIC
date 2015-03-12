#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, binascii
reload(sys)
sys.setdefaultencoding('utf-8')

from xml.dom import minidom

from xml.sax.handler import ContentHandler
import xml.sax # Modulo que analiza sintacticamente un archivo xml

xml_analizador = xml.sax.make_parser() # Objeto parse que va a analizar el fichero

xml_analizador.setContentHandler(ContentHandler()) # Manejador de contenido

nombre_fichero = "ficherocsv.xml"

# Controla que la sintaxis del fichero xml sea correcta
try:
  xml_analizador.parse(nombre_fichero) # Analizamos el fichero
  print("\nEl fichero XML " + nombre_fichero + " está bien formado.")

except getopt.GetoptError as err:
  print ("\nError " + err + ":\n\t " + nombre_fichero + " no es un fichero bien formado")

#Obtenemos el documento completo
xml_documento = minidom.parse(nombre_fichero)
nodos = xml_documento.childNodes

#El comentario de debajo es un ejemplo de la estructura que hay que seguir para obtener el valor de un atributo
#lista = nodos[0].getElementsByTagName("element")[0].attributes.get("name").value
#print(lista)

#Lista de todos los nodos de tipo "element"
lista = nodos[0].getElementsByTagName("Row")

outservices = open("servicios.xml","w")
outgroups = open("groups.xml","w")
outcriticgroups = open("criticidad.xml","w")
outrolegroups = open("roles.xml","w")

id_array=[]
service_group=[]
service_critic_group=[]
service_role_group=[]
groupArray=[]
groupCriticArray=[]
groupRoleArray=[]


xmlstrii=""
xmlstriii=""
attr = []

# Funcion que realiza la carga inicial de servicios y genera el contenido del fichero servicios.xml
def carga():
 xmlfinal= ""
 for nodo in lista:
  if(nodo == lista[0]):
   listahijos = nodo.getElementsByTagName("Data")
   for hijo in listahijos:
     attr.append(hijo.firstChild.nodeValue)
  else:
   listahijos = nodo.getElementsByTagName("Data")
   field = 0
  
   for hijo in listahijos:
     if(field == 0):
      codigoCrue = hijo.firstChild.nodeValue
     elif(field == 1):
      grupoServicio = hijo.firstChild.nodeValue
     elif(field == 2):
      nombreServicio = hijo.firstChild.nodeValue
     elif(field == 3):
      descripcion = hijo.firstChild.nodeValue
      identi = binascii.b2a_hex(os.urandom(4))
      while identi in id_array:
       identi = binascii.b2a_hex(os.urandom(4))
      id_array.append(identi)
     elif(field == 4):
      grupoCritico = hijo.firstChild.nodeValue
     elif(field in ([5,6,7,8,9])):
      acceso = hijo.firstChild.nodeValue
      if(acceso in ["SÍ","Sí","sí","SI","Si","si","YES","Yes","yes","y"]):
       service_role_group.append([identi,attr[field]])
      
     field += 1

      
   if (field != 0):
    service_critic_group.append([identi,grupoCritico])
    service_group.append([identi,grupoServicio])
   
    if grupoServicio not in groupArray:
     groupArray.append(grupoServicio)
   
    if grupoCritico not in groupCriticArray:
     groupCriticArray.append(grupoCritico)

    xmlstring =  """
       <element xsi:type="archimate:BusinessService" id=\""""+ str(identi) +"""\" name=\" """+ str(nombreServicio) +"""\">
         <property key="Código CRUE" value=\""""+ str(codigoCrue) + """\"/>
         <property key="Descripción" value=\""""+ str(descripcion) + """\"/>
       </element> """	

    xmlfinal += xmlstring 
 outservices.write(xmlfinal)
 outservices.close()

# Generacion del fichero groups.xml
def generateGroupsXML():
 xmlstr=""
 for i in groupArray:
   identi = binascii.b2a_hex(os.urandom(4))
   while identi in id_array:
    identi = binascii.b2a_hex(os.urandom(4))
   id_array.append(identi) 
   identi2 = binascii.b2a_hex(os.urandom(4))
 
   xmlstr +="""
      <child xsi:type="archimate:Group" id=\""""+ identi +"""\" name=\""""+ i +"""\">
        <bounds x="-96" y="180" width="325" height="169"/>"""
        
   for j in service_group:
    if(i == j[1]):
     while identi2 in id_array:
      identi2 = binascii.b2a_hex(os.urandom(4))
     id_array.append(identi2)
    
     xmlstr += """
        <child xsi:type="archimate:DiagramObject" id=\"""" + identi2 + """\" textAlignment="2" archimateElement=\""""+ j[0] +"""\">
          <bounds x="12" y="84" width="157" height="37"/>
        </child>"""
   xmlstr +="""
      </child> """
      
 outgroups.write(xmlstr)
 outgroups.close()


# Generacion del fichero criticidad.xml
def generateCriticidadXML():
 xmlstrii=""
 for i in groupCriticArray:
   identi = binascii.b2a_hex(os.urandom(4))
   while identi in id_array:
    identi = binascii.b2a_hex(os.urandom(4))
   id_array.append(identi) 
   identi2 = binascii.b2a_hex(os.urandom(4))
 
   xmlstrii +="""
      <child xsi:type="archimate:Group" id=\""""+ identi +"""\" name=\""""+ i +"""\">
        <bounds x="-96" y="180" width="325" height="169"/>"""
        
   for j in service_critic_group:
    if(i == j[1]):
     while identi2 in id_array:
      identi2 = binascii.b2a_hex(os.urandom(4))
     id_array.append(identi2)
    
     xmlstrii += """
        <child xsi:type="archimate:DiagramObject" id=\"""" + identi2 + """\" textAlignment="2" archimateElement=\""""+ j[0] +"""\">
          <bounds x="12" y="84" width="157" height="37"/>
        </child>"""
   xmlstrii +="""
      </child> """
      
 outcriticgroups.write(xmlstrii)
 outcriticgroups.close()

# Generacion del fichero roles.xml
def generateRolesXML():
 xmlstriii=""	
 for j in service_role_group:
   if j[1] not in groupRoleArray:
    groupRoleArray.append(j[1])


 for i in groupRoleArray:
   identi = binascii.b2a_hex(os.urandom(4))
   while identi in id_array:
    identi = binascii.b2a_hex(os.urandom(4))
   id_array.append(identi) 
   identi2 = binascii.b2a_hex(os.urandom(4))
 
   xmlstriii +="""
      <child xsi:type="archimate:Group" id=\""""+ identi +"""\" name=\""""+ i +"""\">
        <bounds x="-96" y="180" width="325" height="169"/>"""
        
   for j in service_role_group:
    if(i == j[1]):
     while identi2 in id_array:
      identi2 = binascii.b2a_hex(os.urandom(4))
     id_array.append(identi2)
    
     xmlstriii += """
        <child xsi:type="archimate:DiagramObject" id=\"""" + identi2 + """\" textAlignment="2" archimateElement=\""""+ j[0] +"""\">
          <bounds x="12" y="84" width="157" height="37"/>
        </child>"""
   xmlstriii +="""
      </child> """
      
 outrolegroups.write(xmlstriii)
 outrolegroups.close()
 
 # Generacion del fichero Archi.archimate que ya contiene la informacion de los ficheros .xml
def generateArchimate():

 sample = open("Archi_Sample.archimate")
 outstring = str(sample.read())
 outfile = open("Archi.archimate","w")
 
 services = open("servicios.xml","r")
 groups = open("groups.xml","r")
 roles = open("roles.xml","r")
 critic = open("criticidad.xml","r")
 
 servicestring = services.read()
 groupstring = groups.read()
 rolestring = roles.read()
 criticstring = critic.read()

 outstring = outstring.replace("servicios.xml",servicestring)
 outstring = outstring.replace("groups.xml", groupstring)  
 outstring = outstring.replace("roles.xml", rolestring)
 outstring = outstring.replace("criticidad.xml", criticstring)
 
 outfile.write(outstring)
 

carga()
generateGroupsXML()
generateCriticidadXML()
generateRolesXML()
generateArchimate()
