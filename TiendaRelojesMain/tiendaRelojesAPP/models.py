from django.db import models

# Create your models here.
class Filtro(models.Model):
    precio = models.CharField(max_length=30, null=True)
    mecanismo = models.CharField(max_length=30, null=True)
    tipoCorrea = models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.nombreTipo

class Reloj(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.FloatField()
    Filtro = models.ManyToManyField(Filtro)
    def __str__(self):
        return self.marca + ' - ' + self.nombre
    
class Compra(models.Model):
    precioCompra = models.FloatField()
    Reloj = models.ManyToManyField(Reloj)
    def __str__(self):
        return str(self.id) + ': ' + self.Reloj + ' ' + str(self.precioCompra) + '€'
