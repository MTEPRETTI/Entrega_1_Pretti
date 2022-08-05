from django.db import models

# Create your models here.

class Autos(models.Model):

    marca = models.CharField(max_length=40)
    modelo = models.CharField(max_length=40)
  
class Agencia(models.Model):

    rsoc = models.CharField(max_length=40)
    zona = models.CharField(max_length=40)
    
class Vendedor(models.Model):

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    