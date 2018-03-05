from django import forms
from .models import Enlace

#-- --------------------- Formulario Index ---------------------------- -->
#-- ----- Recibir Datos ----- -->
class FormIndex(forms.ModelForm):
	class Meta:
		model = Enlace
		fields = ["nombre","enlace","descripcion","logo"]
class RegFormIndex(forms.Form):
	nombre = forms.CharField(max_length=30)
	enlace = forms.CharField(max_length=150)
	descripcion = forms.CharField(max_length=150)
	logo = forms.CharField(max_length=150)
