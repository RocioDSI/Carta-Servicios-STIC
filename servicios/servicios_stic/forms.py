from django import forms

class UploadForm(forms.Form):
 Nombre_Universidad_Corto = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": 'form-control'}))
 Nombre_Universidad = forms.CharField(max_length=100, widget=forms.TextInput(attrs={"class": 'form-control'}))
 docfile = forms.FileField(
   label='Selecciona el modelo Archimate'
 )   
 imagefile = forms.FileField(
   label='Seleccione el Logo'
 )  
