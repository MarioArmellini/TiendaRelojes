from django.contrib import admin
from .models import *
from .models import Compra, Reloj


# Register your models here.
admin.site.register(Filtro)
admin.site.register(Reloj)

@admin.register(Compra)
class CompraAdmin(admin.ModelAdmin):
    list_display = ('id', 'precioCompra', 'mostrar_relojes')
    filter_horizontal = ('relojes',)

    def save_model(self, request, obj, form, change):
        super().save_model(request, obj, form, change)
        # Aseguramos que el precio total se calcule correctamente después de guardar
        obj.precioCompra = obj.calcular_precio_total()
        obj.save()

    def mostrar_relojes(self, obj):
        return ", ".join([str(reloj) for reloj in obj.relojes.all()])
    mostrar_relojes.short_description = "Relojes"
