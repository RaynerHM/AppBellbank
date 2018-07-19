from django.shortcuts import render

# from .forms import FormIndex, FormSysAdmin, FormSysadminQA, FormSysadminPRO
from django.contrib.auth.models import User
from .models import EnlaceBellbank, Departamento
from django.conf import settings


#-- --------------------- Vistas Generales para el Publico --------------------- -->
def Index(request, department=None):
	app = request.GET.get('app', '')
	departamento = Departamento.objects.order_by('departamento')
	if department:
		resultado = EnlaceBellbank.objects.filter(permiso__permisos='Publico',
		departamento__departamento__contains=department).order_by('nombre')
	else:
		if app != "":
			resultado = EnlaceBellbank.objects.filter(nombre__contains=app,
			permiso__permisos='Publico').order_by('nombre')
		else:			
			resultado = EnlaceBellbank.objects.filter(
			permiso__permisos='Publico').order_by('nombre')
	context = {
		'resultado': resultado,
		'departamento': departamento,
		'MEDIA_URL': settings.MEDIA_URL
	}
	return render(request, "index.html", context)




#-- --------------------- Vistas para Administrador --------------------- -->
def SysAdmin(request, department=None):
	app = request.GET.get('app', '')

	departamento = Departamento.objects.all().order_by('departamento')
	if department:
		resultado = EnlaceBellbank.objects.filter(
			departamento__departamento__contains=department).order_by('nombre')
	else:
		if app != "":
			resultado = EnlaceBellbank.objects.filter(nombre__contains=app).order_by('nombre')
		else:
			resultado = EnlaceBellbank.objects.order_by('nombre')
	context = {
		'resultado': resultado,
		'departamento': departamento,
		'MEDIA_URL': settings.MEDIA_URL
	}
	return render(request, "sysadmin.html", context)


"""
	# resultado = EnlaceBellbank.objects.all().order_by('nombre')
	# return render(request, "sysadmin.html", {
	# 	'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def SysAdminQA(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En QA').order_by('nombre')
	return render(request, "sysadmin.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def SysAdminPro(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En Produccion'
	).order_by('nombre')
	return render(request, "sysadmin.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})
"""
