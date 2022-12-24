from django.db import models

# Create your models here.

class Vehiculo(models.Model):
    marca=models.CharField(max_length=40)
    modelo=models.CharField(max_length=40)
    año=models.IntegerField()
    
class Categoria (models.Model):
    tipo_vehiculo=models.CharField(max_length=40)
    combustible=models.CharField(max_length=40)
    cilindrada_motor=models.CharField(max_length=40)
    
class Vendedor(models.Model):
    nombre=models.CharField(max_length=40)
    telefono=models.IntegerField()
    correo=models.EmailField()