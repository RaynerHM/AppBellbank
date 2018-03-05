from django.contrib import admin

# Register your models here.
from .models import EnlaceCursos, EnlaceBellbank

class AdminEnlace(admin.ModelAdmin):
	#list_display = ["__unicode__","nombre","timestamp"]
	list_display = ["nombre","enlace","descripcion","logo"]

	class Meta:
		model = EnlaceCursos

admin.site.register(EnlaceCursos, AdminEnlace)
admin.site.register(EnlaceBellbank, AdminEnlace)