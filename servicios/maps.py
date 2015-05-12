#!/usr/bin/python
# -*- coding: utf-8 -*-

#
#    Copyright 2014-2015
#
#      STIC - Universidad de La Laguna (ULL) <gesinv@ull.edu.es>
#
#    This file is part of Modelado de Servicios TIC.
#
#    Modelado de Servicios TIC is free software: you can redistribute it and/or modify it under
#    the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    Modelado de Servicios TIC is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with Modelado de Servicios TIC.  If not, see
#    <http://www.gnu.org/licenses/>.
#

import funcionesxml
funcionesxml.inicializacion()

def generaKML():
  kmlstring = """<?xml version="1.0" encoding="UTF-8"?>
<kml xmlns="http://www.opengis.net/kml/2.2">
<Document>	
	<Style id="stic_icon">
		<IconStyle>
			<Icon>
				<href>IconMap.jpg</href>
			</Icon>
		</IconStyle>
	</Style>
"""
  fichero = open("maps.kml","w")
  for i in funcionesxml.SondaArray:

    kmlstring += """      <Placemark>
        <name>""" + i[3][0] + """</name>
        <description> """ + i[3][1] + """</description>
        <styleUrl>#stic_icon</styleUrl>
        <Point>
          <coordinates>"""+ i[3][2] +""",0</coordinates>
        </Point>
      </Placemark>
"""
  kmlstring += """       </Document>
</kml>
"""
  fichero.write(kmlstring)
  fichero.close()   
  
generaKML()
print "Se ha generado el fichero maps.kml con la ubicación de las sondas"
