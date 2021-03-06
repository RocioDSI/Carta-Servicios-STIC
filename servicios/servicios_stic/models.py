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

from django.db import models
import os, sys

# Create your models here.
def content_file_name(instance, filename):
    os.remove('/'.join(["Archi_Upload.archimate"]))
    return '/'.join(["Archi_Upload.archimate"])

def content_image_name(instance, filename):
    os.remove('/'.join(['servicios_stic','css',"Logo.jpg"]))
    return '/'.join(['servicios_stic','css',"Logo.jpg"])

class Document(models.Model):
  filename = models.CharField(max_length=100)
  docfile = models.FileField(upload_to=content_file_name)
  imagefile = models.FileField(upload_to=content_image_name)

  def delete():
	os.remove(os.path.join(settings.MEDIA_ROOT, self.docfile.name))
