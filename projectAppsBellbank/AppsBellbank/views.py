from django.shortcuts import render

from .forms import FormIndex, FormSysAdmin, FormSysadminQA, FormSysadminPRO

from django.contrib.auth.models import User
from .models import EnlaceBellbank


#-- --------------------- Vista General para Usuario --------------------- -->
def Index(request):
	resultado = EnlaceBellbank.objects.all().filter(permiso__permisos='Usuario')
	return render(request, "index.html", {'resultado': resultado})

def IndexQA(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En QA').filter(permiso__permisos='Usuario')
	return render(request, "index.html", {'resultado': resultado})

def IndexPro(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En Produccion').filter(permiso__permisos='Usuario')
	return render(request, "index.html", {'resultado': resultado})


#-- --------------------- Vista para Administrador --------------------- -->
def SysAdmin(request):
	resultado = EnlaceBellbank.objects.all()
	return render(request, "sysadmin.html", {'resultado': resultado})

def SysAdminQA(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En QA')
	return render(request, "sysadmin.html", {'resultado': resultado})

def SysAdminPro(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En Produccion')
	return render(request, "sysadmin.html", {'resultado': resultado})





# def IndexSysAdmin(request):
# 	form = FormSysAdmin(request.POST)
# 	if form.is_valid():
# 		form_data = form.cleaned_data
# 		v_nombre = form_data.get("estado")
# 		print(v_nombre)
# 		resultado = EnlaceBellbank.objects.filter(estado__estado=v_nombre).filter(permiso__permisos='Administrador')
# 		return render(request, "sysadmin.html", {"el_form": form}, resultado)
# 	# context = {
# 	# 	"el_form": form,
# 	# }
# 	# return render(request, "sysadmin.html", context)


def Modificar(request):
	# form = FormModificar(request.POST)
	# if form.is_valid():
		# form_data = form.cleaned_data
		# v_nombre = form_data.get("nombre")
		# v_enlace = form_data.get("enlace")
		# v_descripcion = form_data.get('descripcion')
		# v_logo = form_data.get('logo')

	# 	obj = EnlaceBellbank.objects.create(nombre=v_nombre,
	# 	                            enlace=v_enlace, 
 #                                    descripcion=v_descripcion, 
	# 	                            logo=v_logo
	# 	                            )
	# context = {
	# 	"el_form": form,
	# }
	# return render(request, "modificar.html", context)
	resultado = EnlaceBellbank.objects.all()
	return render(request, "modificar.html", {'resultado': resultado})