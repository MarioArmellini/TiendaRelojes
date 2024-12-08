from django.contrib import admin
from .models import *
from .models import Compra, Reloj


# Register your models here.
admin.site.register(Filtro)
admin.site.register(Reloj)

# Registra una compra actualizando el precio total
@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'precioCompra', 'mostrar_relojes')
    filter_horizontal = ('relojes',)

    def save_model(self, request, obj, form, change):
        # Antes de guardar, recalculamos el precio total de la compra
        obj.precioCompra = obj.calcular_precio_total()
        super().save_model(request, obj, form, change)

    def mostrar_relojes(self, obj):
        return ", ".join([str(reloj) for reloj in obj.relojes.all()])
    mostrar_relojes.short_description = "Relojes"