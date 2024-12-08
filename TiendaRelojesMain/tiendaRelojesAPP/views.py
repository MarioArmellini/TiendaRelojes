from django.shortcuts import render

from django.template import loader
from django.views import generic
from django.http import HttpResponse
from .models import *

# uso de AJAX 
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import Reloj

# vue
from rest_framework.permissions import AllowAny
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Contact  # Importa tu modelo de Contact
from .serializers import ContactSerializer  # Asegúrate de tener un serializer para Contact


class IndexView(generic.TemplateView):
    template_name = 'index.html'

class RelojesListView(generic.ListView):
    template_name = 'relojes.html'
    model = Reloj
    context_object_name = 'relojes'

class RelojesView(generic.DetailView):
    template_name = 'relojDetalle.html'
    model = Reloj
    context_object_name = 'reloj'

class CompraListView(generic.ListView):
    template_name = 'compra.html'
    model = Compra
    context_object_name = 'compras'
    
class CompraView(generic.DetailView):
    template_name = 'compraDetalle.html'
    model = Reloj
    context_object_name = 'compra'

class CarritoListView(generic.ListView):
    template_name = 'carrito.html'
    model = Compra
    context_object_name = 'carrito'    

# Devuelve los detalles del reloj 
def reloj_detalle_ajax(_, pk):
    try:
        reloj = Reloj.objects.get(pk=pk)
        data = {
            'nombre': reloj.nombre,
            'marca': reloj.marca,
            'precio': reloj.precio,
        }
        return JsonResponse(data)
    except Reloj.DoesNotExist:
        return JsonResponse({'error': 'Reloj no encontrado'}, status=404)
    
def vue_app(request):
    return render(request, 'indexVue.html')

class ContactViewSet(ModelViewSet):
    """
    API ViewSet para gestionar contactos.
    """
    queryset = Contact.objects.all()  # Recupera todos los contactos
    serializer_class = ContactSerializer  # Usa el serializer para Contact
    permission_classes = [AllowAny] 