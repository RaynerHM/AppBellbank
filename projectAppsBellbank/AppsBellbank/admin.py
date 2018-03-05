from django.contrib import admin

# Register your models here.
from .models import Enlace

class AdminEnlace(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["nombre","enlace","descripcion","logo"]

	class Meta:
		model = Enlace

admin.site.register(Enlace, AdminEnlace)