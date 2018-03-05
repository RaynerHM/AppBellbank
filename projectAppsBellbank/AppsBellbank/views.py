from django.shortcuts import render

from .forms import FormIndex

from django.contrib.auth.models import User
from .models import Enlace

#-- --------------------- Vista Generar Codigo --------------------- -->
def index(request):
	resultado = Enlace.objects.all()
	# print(resultado)
	return render(request, "index.html", {'resultado': resultado})
	#return render(request, "index.html")

def Modificar(request):
	form = FormModificar(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_nombre = form_data.get("nombre")
		v_enlace = form_data.get("enlace")
		v_descripcion = form_data.get('descripcion')
		v_logo = form_data.get('logo')

		obj = Enlace.objects.create(nombre=v_nombre,
		                            enlace=v_enlace, 
                                    descripcion=v_descripcion, 
		                            logo=v_logo
		                            )
	context = {
		"el_form": form,
	}
	return render(request, "modificar.html", context)
