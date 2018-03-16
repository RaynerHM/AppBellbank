from django.contrib import admin

# Register your models here.
from .models import EnlaceBellbank, Estados, Permisos

class AdminEnlace(admin.ModelAdmin):
	list_display = ["nombre","enlace","descripcion","logo","estado","permiso"]

	class Meta:
		model = EnlaceBellbank

admin.site.register(EnlaceBellbank, AdminEnlace)


class AdminEstados(admin.ModelAdmin):
	list_display = ["estado"]

	class Meta:
		model = Estados

admin.site.register(Estados, AdminEstados)


class AdminPermisos(admin.ModelAdmin):
	list_display = ["permisos"]

	class Meta:
		model = Permisos

admin.site.register(Permisos, AdminPermisos)