from django.shortcuts import render

from .forms import FormIndex, FormSysadmin

from django.contrib.auth.models import User
from .models import EnlaceCursos, EnlaceBellbank

#-- --------------------- Vista Generar Codigo --------------------- -->
def Index(request):
	# resultado = EnlaceBellbank.objects.all()
	# return render(request, "index.html", {'resultado': resultado})
#--------------------------------------------------------------------------------
	# resultado = EnlaceBellbank.objects.filter(nombre="Zimbra")
	resultado = EnlaceBellbank.objects.filter(estado__icontains="En QA")
	# resultado = EnlaceBellbank.objects.all().filter(estado__icontains="En Produccion")
	return render(request, "index.html", {'resultado': resultado})


def Modificar(request):
	form = FormModificar(request.POST)
	if form.is_valid():
		form_data = form.cleaned_data
		v_nombre = form_data.get("nombre")
		v_enlace = form_data.get("enlace")
		v_descripcion = form_data.get('descripcion')
		v_logo = form_data.get('logo')

		obj = EnlaceBellbank.objects.create(nombre=v_nombre,
		                            enlace=v_enlace, 
                                    descripcion=v_descripcion, 
		                            logo=v_logo
		                            )
	context = {
		"el_form": form,
	}
	return render(request, "modificar.html", context)

def Sysadmin(request):
	resultado = EnlaceBellbank.objects.all()
	# print(resultado)
	return render(request, "sysadmin.html", {'resultado': resultado})
	#return render(request, "index.html")