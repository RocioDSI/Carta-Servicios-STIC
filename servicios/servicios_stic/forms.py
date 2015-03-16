from django import forms

class UploadForm(forms.Form):
 Nombre_Universidad_Corto = forms.CharField(max_length=100)
 Nombre_Universidad = forms.CharField(max_length=100)
 docfile = forms.FileField(
   label='Selecciona el modelo Archimate'
 )   
 imagefile = forms.FileField(
   label='Seleccione el Logo'
 )  
