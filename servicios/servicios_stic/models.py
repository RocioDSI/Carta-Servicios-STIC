from django.db import models

# Create your models here.
def content_file_name(instance, filename):
    return '/'.join(["Archi_Upload.archimate"])

def content_image_name(instance, filename):
    return '/'.join(['servicios_stic','css','Logo'])

class Document(models.Model):
  filename = models.CharField(max_length=100)
  docfile = models.FileField(upload_to=content_file_name)
  imagefile = models.FileField(upload_to=content_image_name)
