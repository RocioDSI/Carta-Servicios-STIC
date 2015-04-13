#!/usr/bin/python
# -*- coding: utf-8 -*-

import unittest
import funcionesxml

funcionesxml.inicializacion()

class TestXMLReading(unittest.TestCase):
  funcionesxml.inicializacion()
  def test_groups_1(self):
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Grabación y Difusión de eventos")),"Soporte TIC a la Docencia")
 
  def test_groups_2(self):     
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Soporte a eventos especiales")), "Soporte TIC a la Docencia")

  def test_groups_3(self):
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Gestión de licencias software para docencia ")), "Soporte TIC a la Docencia")

  def test_groups_4(self):
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Conexión Externo a Red de Comunicaciones")), "Soporte TIC a la Gestión")

  def test_groups_5(self):
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Gestión de Certificados")), "Soporte TIC a la Gestión")

  def test_groups_6(self):    
   self.assertEqual(funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Conexión Externo a Red de Comunicaciones")), "Soporte TIC a la Gestión")

  def test_critic_1(self):
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Asesoramiento adquisición infraestructuras y servicios TIC para investigación")), "Alta")
    
  def test_critic_2(self):    
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Conexión Externo a Red de Comunicaciones")), "Alta")
    
  def test_critic_3(self):    
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Gestión de Certificados")), "Alta")
    
  def test_critic_4(self):    
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Gestión de licencias software para docencia ")), "Baja")
    
  def test_critic_5(self):    
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Grabación y Difusión de eventos")), "Baja")
    
  def test_critic_6(self):    
   self.assertEqual(funcionesxml.getServiceCritic(funcionesxml.getBusinessServiceID("Soporte a eventos especiales")), "Baja")
      
  def test_role_1(self):
   self.assertEqual(funcionesxml.getGroupName((funcionesxml.getServiceRoles(funcionesxml.getBusinessServiceID("Gestión de Certificados")))[0]), "PDI")
    
  def test_role_2(self):  
   self.assertEqual(funcionesxml.getGroupName((funcionesxml.getServiceRoles(funcionesxml.getBusinessServiceID("Asesoramiento adquisición infraestructuras y servicios TIC para investigación")))[0]), "PDI")
  
  def test_role_3(self):    
   self.assertEqual(funcionesxml.getGroupName((funcionesxml.getServiceRoles(funcionesxml.getBusinessServiceID("Grabación y Difusión de eventos")))[0]), "Alumnos")
    
  def test_access_1(self):
   self.assertEqual(funcionesxml.getServiceAccess(funcionesxml.getBusinessServiceID("Conexión Externo a Red de Comunicaciones")), "Internet")

  def test_access_2(self):    
   self.assertEqual(funcionesxml.getServiceAccess(funcionesxml.getBusinessServiceID("Gestión de licencias software para docencia ")), "Internet")
    
  def test_access_3(self):    
   self.assertEqual(funcionesxml.getServiceAccess(funcionesxml.getBusinessServiceID("Asesoramiento adquisición infraestructuras y servicios TIC para investigación")), "ULL")
    
  def test_access_4(self):
   self.assertEqual(funcionesxml.getServiceAccess(funcionesxml.getBusinessServiceID("Gestión de Certificados")), "ULL")
    
    
    
suite = unittest.TestLoader().loadTestsFromTestCase(TestXMLReading)
unittest.TextTestRunner(verbosity=2).run(suite)

print funcionesxml.getServiceGroup(funcionesxml.getBusinessServiceID("Soporte a eventos especiales"))
