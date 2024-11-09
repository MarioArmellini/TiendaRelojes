from django.shortcuts import render

from django.template import loader
from django.views import generic
from django.http import HttpResponse
from .models import *
# Create your views here.

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
    model = Compra
    context_object_name = 'compra'
