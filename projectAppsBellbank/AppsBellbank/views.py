from django.shortcuts import render

from .forms import FormIndex, FormSysAdmin, FormSysadminQA, FormSysadminPRO

from django.contrib.auth.models import User
from .models import EnlaceBellbank
from django.conf import settings


#-- --------------------- Vistas Generales para Usuario --------------------- -->
def Index(request):
	resultado = EnlaceBellbank.objects.filter(permiso__permisos='Usuario'
	).order_by('nombre')
	return render(request, "index.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def IndexQA(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En QA').filter(
		permiso__permisos='Usuario')
	return render(request, "index.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def IndexPro(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En Produccion'
	).filter(permiso__permisos='Usuario').order_by('nombre')
	return render(request, "index.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})



#-- --------------------- Vistas para Administrador --------------------- -->
def SysAdmin(request):
	resultado = EnlaceBellbank.objects.all().order_by('nombre')
	return render(request, "sysadmin.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def SysAdminQA(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En QA').order_by('nombre')
	return render(request, "sysadmin.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})

def SysAdminPro(request):
	resultado = EnlaceBellbank.objects.filter(estado__estado='En Produccion'
	).order_by('nombre')
	return render(request, "sysadmin.html", {
		'resultado': resultado, 'MEDIA_URL': settings.MEDIA_URL})
