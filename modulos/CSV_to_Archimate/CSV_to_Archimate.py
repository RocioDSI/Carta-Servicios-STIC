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

id_array=[]
service_group=[]
groupArray=[]
xmlfinal= ""
xmlstr=""

for nodo in lista:
  listahijos = nodo.getElementsByTagName("Data")
  field = 0
  
  for hijo in listahijos:
    if(field == 0):
     codigoCrue = hijo.firstChild.nodeValue
     print ("El codigo CRUE es: " + codigoCrue)
    elif(field == 1):
     grupoServicio = hijo.firstChild.nodeValue
     print ("El Grupo de Servicio es: " + grupoServicio)
    elif(field == 2):
     nombreServicio = hijo.firstChild.nodeValue
     print ("El Servicio es: " + nombreServicio)
    elif(field == 3):
     descripcion = hijo.firstChild.nodeValue
     print ("La descripcion es: " + descripcion)
     identi = binascii.b2a_hex(os.urandom(4))
     while identi in id_array:
      identi = binascii.b2a_hex(os.urandom(4))
     id_array.append(identi)
     print ("El ID es : " + identi + "\n")
    field += 1
    
  if (field != 0):
   service_group.append([identi,grupoServicio])
   if grupoServicio not in groupArray:
    groupArray.append(grupoServicio)
 
   xmlstring =  """
       <element xsi:type="archimate:BusinessService" id=\""""+ str(identi) +"""\" name=\" """+ str(nombreServicio) +"""\">
         <property key="Código CRUE" value=\""""+ str(codigoCrue) + """\"/>
         <property key="Descripción" value=\""""+ str(descripcion) + """\"/>
       </element>"""	
  
   xmlfinal += xmlstring
  
outservices.write(xmlfinal)

for i in groupArray:
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
      </child>"""
      
outgroups.write(xmlstr)

