#!/usr/bin/python
# -*- coding: utf-8 -*-

import funcionesxml


def main():
 funcionesxml.inicializacion()
	
 f = open('datos.csv','w')
 
 for i in funcionesxml.BusinessServiceArray:
  f.write(str(i[0]))
  f.write('\n')
 


main()
	
	
	
	



