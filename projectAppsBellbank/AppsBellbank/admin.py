from django.contrib import admin

# Register your models here.
from .models import EnlaceBellbank, Estados, Permisos, Departamento

class AdminEnlace(admin.ModelAdmin):
	list_display = ["nombre","enlace","descripcion","logo","estado","permiso"]
	ordering = ['nombre']

	class Meta:
		model = EnlaceBellbank

admin.site.register(EnlaceBellbank, AdminEnlace)


class AdminDepartamento(admin.ModelAdmin):
	list_display = ["departamento"]
	ordering = ['departamento']

	class Meta:
		model = Departamento


admin.site.register(Departamento, AdminDepartamento)


class AdminEstados(admin.ModelAdmin):
	list_display = ["estado"]
	ordering = ['estado']

	class Meta:
		model = Estados

admin.site.register(Estados, AdminEstados)


class AdminPermisos(admin.ModelAdmin):
	list_display = ["permisos"]
	ordering = ['permisos']

	class Meta:
		model = Permisos

admin.site.register(Permisos, AdminPermisos)
