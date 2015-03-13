#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, getopt
reload(sys)
sys.setdefaultencoding('utf-8')

from xml.dom import minidom

from xml.sax.handler import ContentHandler
import xml.sax # Modulo que analiza sintacticamente un archivo xml

xml_analizador = xml.sax.make_parser() # Objeto parse que va a analizar el fichero

xml_analizador.setContentHandler(ContentHandler()) # Manejador de contenido

if (len(sys.argv) == 2):
 nombre_fichero = str(sys.argv[1])
else:
 nombre_fichero = "Archi_Upload.archimate"

# Controla que la sintaxis del fichero xml sea correcta
try:
  xml_analizador.parse(nombre_fichero) # Analizamos el fichero
  print("\nEl fichero XML " + nombre_fichero + " está bien formado.")

except:
  print ("\nError:\n\t " + nombre_fichero + " no es un fichero bien formado")
  sys.exit()
  
#Obtenemos el documento completo
xml_documento = minidom.parse(nombre_fichero)
nodos = xml_documento.childNodes

#El comentario de debajo es un ejemplo de la estructura que hay que seguir para obtener el valor de un atributo
#lista = nodos[0].getElementsByTagName("element")[0].attributes.get("name").value
#print(lista)

#Lista de todos los nodos de tipo "element"
lista = nodos[0].getElementsByTagName("element")

#Contenedores para los objetos Archimate
BusinessServiceArray =[]
BusinessRoleArray =[]
AssociationRelationshipArray = []
GroupArray = []
GroupCriticArray = []
GroupRoleArray = []
GroupAccessArray = []
ServicesPerGroupArray = []
ViewsNameArray = []

#Nombre de las vistas
VistaGruposServicios = "Carta de servicios"
VistaRoles = "Roles"
VistaCriticidad = "Criticidad"
VistaAcceso = "Nivel de Acceso"

#Almacenamiento de servicios
def cargaBusinessService():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:BusinessService"):    
    nombre_servicio = nodo.attributes.get("name").value
    id_servicio = nodo.attributes.get("id").value
    listahijos = nodo.getElementsByTagName("property")
    clave = []
    valor = []
    for hijo in listahijos:
      clave.append(hijo.attributes.get("key").value)
      if(hijo.attributes.get("value") != None):
       valor.append(hijo.attributes.get("value").value)     
      else:
       valor.append("Campo Vacío")
    criticidad = ServiceCritic(id_servicio)
    acceso = ServiceAccess(id_servicio)
    if(nombre_servicio not in ["Servicio","Servicio 1","Servicio 2","Servicio 3"]):
     BusinessServiceArray.append([id_servicio,nombre_servicio, clave, valor, criticidad, acceso])
         
#Almacenamiento de roles
def cargaBusinessRole():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:BusinessRole"):
    nombre_rol = nodo.attributes.get("name").value
    id_roles = nodo.attributes.get("id").value
    for i in BusinessRoleArray:
      if (i[0] == id_roles or i[1] == nombre_rol):
         print("ERROR: Nombre de ROL o ID repetido en el modelo")
    BusinessRoleArray.append([id_roles,nombre_rol])
    
#Almacenamiento de las relaciones
def cargaAssociationRelationship():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:AssociationRelationship"):
    id_relacion_asociacion = nodo.attributes.get("id").value
    source = nodo.attributes.get("source").value
    target = nodo.attributes.get("target").value
    AssociationRelationshipArray.append([id_relacion_asociacion,source,target])

#Almacenamiento de los grupos de servicio por Criticidad, Rol o Grupo de Servicio
def cargaGroup():
  for nodo in lista:  
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel")):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
        nombre_grupo = hijo.attributes.get("name").value
        id_grupo = hijo.attributes.get("id").value
        if(nodo.attributes.get("name").value == VistaGruposServicios):
         GroupArray.append([id_grupo,nombre_grupo])
        elif(nodo.attributes.get("name").value == VistaCriticidad):
         GroupCriticArray.append([id_grupo,nombre_grupo])
        elif(nodo.attributes.get("name").value == VistaRoles):
         GroupRoleArray.append([id_grupo,nombre_grupo])
        elif(nodo.attributes.get("name").value == VistaAcceso):
         GroupAccessArray.append([id_grupo,nombre_grupo])
         
#Almacenamiento de todos los servicios por grupo para grupos de Servicio, Criticidad, Roles y Nivel de Acceso      
def BusinessServicePorGroup():
  for nodo in lista:
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and ((nodo.attributes.get("name").value) in [VistaCriticidad,VistaGruposServicios,VistaRoles,VistaAcceso])): 
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
     if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
      id_grupo = hijo.attributes.get("id").value
      listanietos = hijo.getElementsByTagName("child")
      for nieto in listanietos:
       if (nieto.attributes.get("xsi:type").value == "archimate:DiagramObject"):
        for i in BusinessServiceArray:
          if( i[0] == nieto.attributes.get("archimateElement").value):
           id_nieto = nieto.attributes.get("archimateElement").value
           ServicesPerGroupArray.append([str(id_grupo),str(id_nieto)])
                   
#Almacenamiento de Criticidad de Servicio para un servicio concreto
def ServiceCritic(serviceID):
  for nodo in lista:
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and (str(nodo.attributes.get("name").value)) == VistaCriticidad):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
       listanietos = hijo.getElementsByTagName("child")
       for nieto in listanietos:
        id_nieto = nieto.attributes.get("archimateElement").value
        if(serviceID == id_nieto):
         return hijo.attributes.get("name").value
         
#Almacenamiento de nivel de acceso para un servicio concreto
def ServiceAccess(serviceID):
  for nodo in lista:
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and (str(nodo.attributes.get("name").value)) == VistaAcceso):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
       listanietos = hijo.getElementsByTagName("child")
       for nieto in listanietos:
        id_nieto = nieto.attributes.get("archimateElement").value
        if(serviceID == id_nieto):
         return hijo.attributes.get("name").value
         
#Obtencion del nivel de acceso para un servicio
def getServiceAccess(serviceID):
  for i in BusinessServiceArray:
   if (i[0] == serviceID):
    return i[5]
   
#Obtencion del nivel de criticidad para un servicio
def getServiceCritic(serviceID):
  for i in BusinessServiceArray:
   if (i[0] == serviceID):
    return i[4]
                          
# Obtener el grupo de un servicio a partir del identificador de servicio
def getServiceAllGroups(serviceID):
  groups=[]
  for i in ServicesPerGroupArray:
    if(i[1] == serviceID):
     groups.append(i[0])
  return group

# Obtener los servicios de un grupo (de Servicios, Crticidad o por Rol) a través del identificador de grupo
def getGroupServices(groupID):
  services=[]
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
     if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
      if(hijo.attributes.get("id").value == groupID):
       listanietos = hijo.getElementsByTagName("child")
       for nieto in listanietos:
        if (nieto.attributes.get("xsi:type").value == "archimate:DiagramObject"):
         for i in BusinessServiceArray:
          if( i[0] == nieto.attributes.get("archimateElement").value):
           id_nieto = nieto.attributes.get("archimateElement").value
           services.append(id_nieto)
  return services

# Obtener los roles para los que un servicio está disponible
def getServiceRoles(serviceID):
  roles = []
  for i in ServicesPerGroupArray:
   if(serviceID == i[1]):
    for k in GroupRoleArray:
      if(k[0] == i[0]):
       roles.append(i[0])
  return roles


# Obtener el grupo de servicios para un  servicio (ID)
def getServiceGroup(serviceID):
  for i in ServicesPerGroupArray:
   if (i[1] == serviceID):
    for k in GroupArray:
     if (k[0] == i[0]):
      return k[1]

# Obtener los servicios de un rol a traves del identificador de rol
def getRoleServices(roleID):
  j = 1
  for i in AssociationRelationshipArray:
    if (roleID ==  i[1]):
      print("\n"+ str(j)+") " + str(getBusinessServiceName(i[2])))
      j = j+1
    elif (roleID == i[2]):
      print("\n"+ str(j)+") " + str(getBusinessServiceName(i[1])))
      j = j+1

##Obtener nombres a partir de IDs##
def getBusinessRoleName(BusinessRoleID):
  for i in BusinessRoleArray:
   if(BusinessRoleID == i[0]):
    name = i[1]
    return name

def getBusinessServiceName(BusinessServiceID):
  for i in BusinessServiceArray:
    if(BusinessServiceID == i[0]):
      name = i[1]
      return name

def getGroupName(GroupID):
  for i in GroupArray:
    if(GroupID == i[0]):
       name = i[1]
       return name
  for i in GroupRoleArray:
    if(GroupID == i[0]):
       name = i[1]
       return name
  for i in GroupCriticArray:
    if(GroupID == i[0]):
       name = i[1]
       return name
  for i in GroupAccessArray:
    if(GroupID == i[0]):
       name = i[1]
       return name
        
##Obtener IDs a partir de nombres##
def getBusinessRoleID(BusinessRoleName):
  for i in BusinessRoleArray:
   if(BusinessRoleName == i[1]):
    ID = i[0]
    return ID

def getBusinessServiceID(BusinessServiceName):
  for i in BusinessServiceArray:
    if(BusinessServiceName == i[1]):
      ID = i[0]
      return ID

def getGroupID(GroupName):
  for i in GroupArray:
    if(GroupName == i[1]):
       ID = i[0]
       return ID
  for i in GroupCriticArray:
    if(GroupName == i[1]):
       ID = i[0]
       return ID
  for i in GroupRoleArray:
    if(GroupName == i[1]):
       ID = i[0]
       return ID
  

#Devuelve doble lista Key-Value de propiedades de un servicio
def getServiceProperties(serviceID):

  for i in BusinessServiceArray:
   if (i[0] == serviceID):
     key = i[2]
     value = i[3]
  propertylist = [key,value]
  return propertylist

   
def inicializacion():
 cargaBusinessService()
 cargaBusinessRole()
 cargaAssociationRelationship()
 cargaGroup()
 BusinessServicePorGroup()
 runtest()
 
############### TEST ###############
 
def runtest():
  service_nogroup_test()
  service_nocriticgroup_test()
  service_noaccessgroup_test()
  service_multiplegroup_test()
  service_multiplecriticgroup_test()
  service_multipleaccessgroup_test()

  
def service_nogroup_test():
 for i in BusinessServiceArray:
  k = 0
  for j in GroupArray:
   if([j[0],i[0]] in ServicesPerGroupArray):
    k=1
    break
  if (k == 0):
   print " \n [!] WARNING [!] El Servicio "+ i[1] + " no pertenece a ningún Grupo de Servicios \n"

   
def service_nocriticgroup_test():
 for i in BusinessServiceArray:
  k = 0
  for j in GroupCriticArray:
   if([j[0],i[0]] in ServicesPerGroupArray):
    k=1
    break
  if (k == 0):
   print " \n [!] WARNING [!] El Servicio "+ i[1] + " no pertenece a ningún Grupo de Criticidad \n"

def service_noaccessgroup_test():
 for i in BusinessServiceArray:
  k = 0
  for j in GroupAccessArray:
   if([j[0],i[0]] in ServicesPerGroupArray):
    k=1
    break
  if (k == 0):
   print " \n [!] WARNING [!] El Servicio "+ i[1] + " no pertenece a ningún Nivel de Acceso \n"

def service_multiplegroup_test():
 for i in BusinessServiceArray:
  groups = []
  k = 0
  for j in GroupArray:
   if(([j[0],i[0]] in ServicesPerGroupArray) and (k == 0)):
    groups.append(j[0])
    k=1
   elif(([j[0],i[0]] in ServicesPerGroupArray) and (k == 1)):
    groups.append(j[0])
    k=2
   elif(([j[0],i[0]] in ServicesPerGroupArray)):
    groups.append(j[0])
    
   if (k == 2):
    errorMessage = " \n [!] WARNING [!] El Servicio "+ i[1] + " pertenece a varios Grupos de Servicios: "
    for m in groups:
     errorMessage += "[" + getGroupName(m) + "]  "
    print errorMessage


def service_multiplecriticgroup_test():
 for i in BusinessServiceArray:
  groups = []
  k = 0
  for j in GroupCriticArray:
   if(([j[0],i[0]] in ServicesPerGroupArray) and (k == 0)):
    groups.append(j[0])
    k=1
   elif(([j[0],i[0]] in ServicesPerGroupArray) and (k == 1)):
    groups.append(j[0])
    k=2
   elif(([j[0],i[0]] in ServicesPerGroupArray)):
    groups.append(j[0])
    
   if (k == 2):
    errorMessage = " \n [!] WARNING [!] El Servicio "+ i[1] + " pertenece a varios Niveles de Criticidad: "
    for m in groups:
     errorMessage += "[" + getGroupName(m) + "]  "
    print errorMessage

def service_multipleaccessgroup_test():
 for i in BusinessServiceArray:
  groups = []
  k = 0
  for j in GroupAccessArray:
   if(([j[0],i[0]] in ServicesPerGroupArray) and (k == 0)):
    groups.append(j[0])
    k=1
   elif(([j[0],i[0]] in ServicesPerGroupArray) and (k == 1)):
    groups.append(j[0])
    k=2
   elif(([j[0],i[0]] in ServicesPerGroupArray)):
    groups.append(j[0])
   
  if (k == 2):
   errorMessage = " \n [!] WARNING [!] El Servicio "+ i[1] + " pertenece a varios Niveles de Acceso: "
   for m in groups:
    errorMessage += "[" + getGroupName(m) + "]  "
   print errorMessage
