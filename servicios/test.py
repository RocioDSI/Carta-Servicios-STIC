#!/usr/bin/python
# -*- coding: utf-8 -*-

import funcionesxml
from selenium import webdriver
import unittest

def formatstring(nombreGrupo):
  nombrProc = nombreGrupo
  nombrProc=nombrProc.replace("Á","a")
  nombrProc=nombrProc.replace("É","e")
  nombrProc=nombrProc.replace("Í","i")
  nombrProc=nombrProc.replace("Ó","o")
  nombrProc=nombrProc.replace("Ú","u")  
  nombrProc=nombrProc.replace('á','a')
  nombrProc=nombrProc.replace("é","e")
  nombrProc=nombrProc.replace("í","i")
  nombrProc=nombrProc.replace("ó","o")
  nombrProc=nombrProc.replace("ú","u")
  nombrProc=nombrProc.replace("ñ","n")
  nombrProc=nombrProc.replace("ç","c")
  nombrProc=nombrProc.replace("-","_")
  nombrProc=nombrProc.replace(" ","_")
  nombrProc=nombrProc.replace("(","_")
  nombrProc=nombrProc.replace(")","_")
  nombrProc=nombrProc.replace("&","_")
  nombrProc=nombrProc.replace("/","_")
  nombrProc=nombrProc.replace("%","_")
  nombrProc=nombrProc.replace(".","")
  nombrProc=nombrProc.lower()
  return nombrProc

class Pruebas(unittest.TestCase):
  funcionesxml.inicializacion()
  def setUp(self):
    self.browser = webdriver.Firefox()
    
  def tearDown(self):
    self.browser.quit()
    
  def test_titulos_grupos(self):
    for i in funcionesxml.GroupArray:
      url = 'http://localhost:8000/' + formatstring(i[1])
      self.browser.get(url)
      assert 'STIC - Universidad de' in self.browser.title
      header_text = self.browser.find_element_by_tag_name('h1').text
      self.assertEqual(i[1], header_text)
      
  def test_titulos_servicios(self):
    for i in funcionesxml.BusinessServiceArray:
      url = 'http://localhost:8000/' + formatstring(i[1])
      grupo = str(funcionesxml.getServiceGroup(i[0]))
      self.browser.get(url)
      assert 'STIC - Universidad de la Laguna' in self.browser.title
      header_text = self.browser.find_element_by_tag_name('h1').text
      self.assertEqual(str(funcionesxml.getBusinessServiceName(i[0])), str(header_text))

suite = unittest.TestLoader().loadTestsFromTestCase(Pruebas)
unittest.TextTestRunner(verbosity=2).run(suite)
