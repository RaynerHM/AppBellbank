from django import forms
from .models import EnlaceCursos, EnlaceBellbank

#-- --------------------- Formulario Index ---------------------------- -->
#-- ----- Recibir Datos ----- -->
class FormIndex(forms.ModelForm):
	class Meta:
		model = EnlaceBellbank
		fields = ["nombre","enlace","descripcion","logo"]



class FormSysAdmin(forms.ModelForm):
	class Meta:
		model = EnlaceBellbank
		fields = ["nombre","enlace","descripcion","logo"]



class RegFormIndex(forms.Form):
	nombre = forms.CharField(max_length=30)
	enlace = forms.CharField(max_length=150)
	descripcion = forms.CharField(max_length=150)
	logo = forms.CharField(max_length=150)



class FormSysadmin(forms.ModelForm):
	class Meta:
		model = EnlaceBellbank
		fields = ["nombre","enlace","descripcion","logo","estado"]
class FormSysadminQA(forms.ModelForm):
	class Meta:
		model = EnlaceBellbank
		fields = ["nombre","enlace","descripcion","logo","estado"]
class FormSysadminPRO(forms.ModelForm):
	class Meta:
		model = EnlaceBellbank
		fields = ["nombre","enlace","descripcion","logo","estado"]
		

# class RegFormSysadmin(forms.Form):
# 	nombre = forms.CharField(max_length=30)

