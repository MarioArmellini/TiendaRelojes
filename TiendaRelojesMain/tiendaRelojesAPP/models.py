from django.db import models

class Filtro(models.Model):
    RANGO_PRECIOS = [
        ('0-100', '0 a 100€'),
        ('100-500', '100 a 500€'),
        ('500-1000', '500 a 1000€'),
        ('1000-5000', '1000 a 5000€'),
        ('10000+', 'Más de 10000€')
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

    precio = models.CharField(max_length=30, choices=RANGO_PRECIOS, null=True, blank=True)
    tipo_visualizacion = models.CharField(max_length=30, choices=TIPOS_VISUALIZACION, null=True, blank=True)
    tipo_correa = models.CharField(max_length=30, choices=TIPOS_CORREA, null=True, blank=True)

    def __str__(self):
        return f"Filtro: {self.precio}, {self.tipo_visualizacion}, {self.tipo_correa}"


class Reloj(models.Model):
    nombre = models.CharField(max_length=30)
    marca = models.CharField(max_length=30)
    precio = models.FloatField()
    fotoUrl = models.CharField(max_length=250, null=True)
    def __str__(self):
        return f"{self.marca} - {self.nombre}"

class Compra(models.Model):
    precioCompra = models.FloatField(editable=False, null=False, default=0)
    relojes = models.ManyToManyField(Reloj, related_name='compras')

    def calcular_precio_total(self):
        return sum(reloj.precio for reloj in self.relojes.all())

    def save(self, *args, **kwargs):
        # Solo actualizamos `precioCompra` si ya está guardado (no al crearlo)
        if self.pk:
            self.precioCompra = self.calcular_precio_total()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Compra {self.id}: {self.precioCompra}€ - {self.relojes.count()} relojes"

class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.name} - {self.email} - {self.phone}"