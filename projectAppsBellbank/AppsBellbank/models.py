from django.db import models

# Create your models here.
class Estados(models.Model):
	estado = models.CharField(max_length=15, blank=False, null=False)
	def __str__(self):
		return self.estado

class Permisos(models.Model):
	permisos = models.CharField(max_length=15, blank=False, null=False)
	def __str__(self):
		return self.permisos

class Departamento(models.Model):
	departamento = models.CharField(max_length=25, blank=False, null=False)
	def __str__(self):
		return self.departamento
		
class EnlaceBellbank(models.Model):
	nombre = models.CharField(max_length=30, blank=False, null=False)
	enlace = models.CharField(max_length=150, blank=False, null=False)
	descripcion = models.CharField(max_length=150, blank=True, null=True)
	logo = models.ImageField(upload_to='logos/', default = 'logos/logo.jpg' )
	estado = models.ForeignKey('Estados', on_delete=models.CASCADE, blank=True, null=True)
	permiso = models.ForeignKey('Permisos', on_delete=models.CASCADE, blank=True, null=True)
	departamento = models.ManyToManyField(Departamento)
	
	def __str__(self):
    		return str(self.nombre)

