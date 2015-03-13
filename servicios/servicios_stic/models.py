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
