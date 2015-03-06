#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys
reload(sys)
sys.setdefaultencoding('utf-8')

from xml.dom import minidom

from xml.sax.handler import ContentHandler
import xml.sax # Modulo que analiza sintacticamente un archivo xml

xml_analizador = xml.sax.make_parser() # Objeto parse que va a analizar el fichero

xml_analizador.setContentHandler(ContentHandler()) # Manejador de contenido

nombre_fichero = "Archi_Stic1.0.archimate"

# Controla que la sintaxis del fichero xml sea correcta
try:
  xml_analizador.parse(nombre_fichero) # Analizamos el fichero
  print("\nEl fichero XML " + nombre_fichero + " estÃ¡ bien formado.")

except getopt.GetoptError as err:
  print ("\nError " + err + ":\n\t " + nombre_fichero + " no es un fichero bien formado")

#Obtenemos el documento completo
xml_documento = minidom.parse(nombre_fichero)
nodos = xml_documento.childNodes

#El comentario de debajo es un ejemplo de la estructura que hay que seguir para obtener el valor de un atributo
#lista = nodos[0].getElementsByTagName("element")[0].attributes.get("name").value
#print(lista)

#Lista de todos los nodos de tipo "element"
lista = nodos[0].getElementsByTagName("element")


BusinessServiceArray =[]
BusinessRoleArray =[]
AssociationRelationshipArray = []
GroupArray = []
GroupCriticArray = []
ServicesPerGroupArray = []
ViewsNameArray = []

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
    for i in BusinessServiceArray:
        if (i[0] == id_servicio or i[1] == nombre_servicio):
         print("ERROR: Nombre de SERVICIO o ID repetido en el modelo")
         return
    BusinessServiceArray.append([id_servicio,nombre_servicio, clave, valor, criticidad])
    #print("Servicio: " + nombre_servicio + " Id: " + id_servicio)
    
#Almacenamiento de roles
def cargaBusinessRole():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:BusinessRole"):
    nombre_rol = nodo.attributes.get("name").value
    id_roles = nodo.attributes.get("id").value
    for i in BusinessRoleArray:
      if (i[0] == id_roles or i[1] == nombre_rol):
         print("ERROR: Nombre de ROL o ID repetido en el modelo")
         return
    BusinessRoleArray.append([id_roles,nombre_rol])
    #print("Rol: " + nombre_rol + " Id: " + id_roles)
    
#Almacenamiento de las relaciones
def cargaAssociationRelationship():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:AssociationRelationship"):
    id_relacion_asociacion = nodo.attributes.get("id").value
    source = nodo.attributes.get("source").value
    target = nodo.attributes.get("target").value
    AssociationRelationshipArray.append([id_relacion_asociacion,source,target])
    #print("\nLa Id de relacion de asociacion: " + id_relacion_asociacion + " Origen: [" + str(getAnyName(source)) + "] Destino: [" + str(getAnyName(target))+"]")

#Almacenamiento de los grupos de servicio
def cargaGroup():
  for nodo in lista:  
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and nodo.attributes.get("name").value == "Carta de servicios"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
        nombre_grupo = hijo.attributes.get("name").value
        id_grupo = hijo.attributes.get("id").value
        for i in GroupArray:
         if (i[0] == id_grupo or i[1] == nombre_grupo):
          print("ERROR: Nombre de GRUPO DE SERVICIOS o ID repetido en el modelo")
          return
        #print("Grupo: " + nombre_grupo + " Id: " + id_grupo)
        GroupArray.append([id_grupo,nombre_grupo])
        
#Almacenamiento de los grupos de criticidad
def cargaCriticGroup():
  for nodo in lista:  
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and nodo.attributes.get("name").value == "Criticidad"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
        nombre_grupo = hijo.attributes.get("name").value
        id_grupo = hijo.attributes.get("id").value
        for i in GroupCriticArray:
         if (i[0] == id_grupo or i[1] == nombre_grupo):
          print("ERROR: Nombre de GRUPO DE SERVICIOS o ID repetido en el modelo")
          return
        #print("Grupo: " + nombre_grupo + " Id: " + id_grupo)
        GroupCriticArray.append([id_grupo,nombre_grupo])


#Almacenamiento de todos los servicios por grupo        
def BusinessServicePorGroup():
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
     if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
      id_grupo = hijo.attributes.get("id").value
      listanietos = hijo.getElementsByTagName("child")
      for nieto in listanietos:
       if (nieto.attributes.get("xsi:type").value == "archimate:DiagramObject"):
        id_nieto = nieto.attributes.get("archimateElement").value
        ServicesPerGroupArray.append([id_grupo,id_nieto])

#Almacenamiento de Criticidad de Servicio
def ServiceCritic(serviceID):
  for nodo in lista:
   if((nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel") and (str(nodo.attributes.get("name").value)) == "Criticidad"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
      if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
       listanietos = hijo.getElementsByTagName("child")
       for nieto in listanietos:
        id_nieto = nieto.attributes.get("archimateElement").value
        if(serviceID == id_nieto):
         return hijo.attributes.get("name").value

	    
# Obtener el grupo de un servicio a partir del identificador de servicio
def getServiceGroup(serviceID):
  for nodo in lista:
   if(nodo.attributes.get("xsi:type").value == "archimate:ArchimateDiagramModel"):
    listahijos = nodo.getElementsByTagName("child")
    for hijo in listahijos:
     if (hijo.attributes.get("xsi:type").value == "archimate:Group"):
      id_grupo = hijo.attributes.get("id").value
      listanietos = hijo.getElementsByTagName("child")
      for nieto in listanietos:
       if (nieto.attributes.get("xsi:type").value == "archimate:DiagramObject"):
        id_nieto = nieto.attributes.get("archimateElement").value
        if (id_nieto == serviceID): 
         print ("\n El servicio " + str(getBusinessServiceName(serviceID)) +" pertenece al grupo " + str(getGroupName(id_grupo)))

# Obtener los servicios de un grupo a travÃ©s del identificador de grupo
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
         id_nieto = nieto.attributes.get("archimateElement").value
         services.append(id_nieto)
  return services
            	    
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

# Visualizacion de Grupos
def showGroups():
  j = 1
  for i in GroupArray:
   print("\n"+ str(j)+") " + i[1])
   j = j+1
   
# Visualizacion de Servicios
def showServices():
  j = 1
  for i in BusinessServiceArray:
    print("\n"+ str(j)+") " + i[1])
    j = j+1
    
# Visualizacion de Roles
def showRoles():
  j = 1
  for i in BusinessRoleArray:
   print("\n"+ str(j)+") " + i[1])
   j = j+1
  
# Visualizacion de Relaciones Source->Target
def showRelation():
  j = 1;
  for i in AssociationRelationshipArray:
    print("\n"+ str(j)+") " + getAnyName(i[1]) + " >>>> " + getAnyName(i[2]))
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
     
def getAnyName(ID):
  for i in BusinessRoleArray:
   if(ID == i[0]):
    name = i[1]
    return name
  for i in BusinessServiceArray:
    if(ID == i[0]):
      name = i[1]
      return name
  for i in GroupArray:
    if(ID == i[0]):
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
  
def getAnyID(name):
  for i in BusinessRoleArray:
   if(name == i[1]):
    ID = i[0]
    return name
  for i in BusinessServiceArray:
    if(name == i[1]):
      ID = i[0]
      return ID
  for i in GroupArray:
    if(ID == i[1]):
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




#Menu para aplicacion en Consola
def menu():
  clear = lambda: os.system('clear')
  clear()
  
  x = 0
  while (x == 0):
   clear = lambda: os.system('clear')
   clear()
   print("\n Menu \n 1) Listar grupos \n 2) Listar todos los servicios \n 3) Listar todos los roles \n 4) Mostrar todas las relaciones \n 9) Salir")
   try:
     n=int(raw_input('Opcion:'))
   except ValueError:
     print "Not a number"
  
   if (n == 1):
     clear()
     print( "\n Seleccione un grupo para ver sus servicios") 
     showGroups();
     try:
       n=int(raw_input('Opcion:'))
     except ValueError:
       print "Not a number"
     clear()
     getGroupServices(str(GroupArray[n-1][0]))  
   
     
   elif(n == 2):
     clear()
     print( "\n Seleccione un servicio para ver a que grupo pertenece")
     showServices()
     try:
       n=int(raw_input('Opcion:'))
     except ValueError:
       print "Not a number"
     clear()
     getServiceGroup(str(BusinessServiceArray[n-1][0])) 

   
   elif(n == 3):
    clear()
    print( "\n Seleccione un rol para ver que servicios le corresponde")
    showRoles()
    try:
       n=int(raw_input('Opcion:'))
    except ValueError:
       print "Not a number"
    clear()
    getRoleServices(BusinessRoleArray[n-1][0])
    
   elif(n == 4):
     clear()
     showRelation()
   elif(n == 9):
     x = 1
     
   raw_input('\n \n Pulsa cualquier tecla para continuar')
   
def inicializacion():
 cargaBusinessService()
 cargaBusinessRole()
 cargaAssociationRelationship()
 cargaGroup()
 cargaCriticGroup()
 BusinessServicePorGroup()

 
