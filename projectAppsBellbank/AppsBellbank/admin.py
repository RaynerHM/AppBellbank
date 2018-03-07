from django.contrib import admin

# Register your models here.
from .models import EnlaceCursos, EnlaceBellbank, Estados

class AdminEnlace(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["nombre","enlace","descripcion","logo",'estado']

	class Meta:
		model = EnlaceBellbank

admin.site.register(EnlaceBellbank, AdminEnlace)

class AdminCursos(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["nombre","enlace","descripcion","logo"]

	class Meta:
		model = EnlaceCursos

admin.site.register(EnlaceCursos, AdminCursos)

class AdminEstados(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["estado"]

	class Meta:
		model = Estados

admin.site.register(Estados, AdminEstados)
