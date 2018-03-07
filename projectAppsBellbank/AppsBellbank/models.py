from django.db import models

# Create your models here.
class Estados(models.Model):
	estado = models.CharField(max_length=15, blank=False, null=False)
	def __str__(self):
			return self.estado

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
	estado = models.ForeignKey('Estados', on_delete=models.CASCADE, blank=True, null=True)
	
	def __str__(self):
		return str(self.nombre)
		 
		
		# if es == 'En Produccion':
		# 	return str(self.estado)
				