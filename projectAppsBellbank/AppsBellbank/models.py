from django.db import models

# Create your models here.
class EnlaceCursos(models.Model):
	nombre = models.CharField(max_length=30, blank=False, null=False)
	enlace = models.CharField(max_length=150, blank=False, null=False)
	descripcion = models.CharField(max_length=150, blank=True, null=True)
	logo = models.CharField(max_length=150, blank=True, null=True)

class EnlaceBellbank(models.Model):
	nombre = models.CharField(max_length=30, blank=False, null=False)
	enlace = models.CharField(max_length=150, blank=False, null=False)
	descripcion = models.CharField(max_length=150, blank=True, null=True)
	logo = models.CharField(max_length=150, blank=True, null=True)