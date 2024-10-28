from django.db import models

# Create your models here.
class Filtro(models.Model):
    RANGO_PRECIOS = [
        ('0-100', '0 a 100€'),
        ('100-500', '100 a 500€'),
        ('500-1000', '500 a 1000€')
        ('1000-5000', '1000 a 5000€')
        ('10000+', 'Más de 10000€€')
    ]
    TIPOS_VISUALIZACION = [
        ('Digital', 'Digital'),
        ('Analogico', 'Analógico')
    ]
    TIPOS_CORREA = [
        ('Acero', 'Acero'),
        ('Cuero', 'Cuero'),
        ('Tela', 'Tela')
    ]

    precio = models.CharField(max_length=30, choices=RANGO_PRECIOS, null=True)
    tipo_visualizacion = models.CharField(max_length=30, choices=TIPOS_VISUALIZACION, null=True)
    tipo_correa = models.CharField(max_length=30, choices=TIPOS_CORREA, null=True)

    def __str__(self):
        return f"Filtro: {self.precio}, {self.tipo_visualizacion}, {self.tipo_correa}"

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
