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
    context_object_name = 'relojes'

class CompraListView(generic.ListView):
    template_name = 'compra.html'
    model = Compra
class CompraView(generic.DetailView):
    template_name = 'compraDetalle.html'
    model = Compra
"""""
#def index(request):
#    return HttpResponse("Hello, world!")

def home(request):
    return render(request, 'index.html')

#def index(request):
#    return render(request, 'index.html')

def examples(request):
    return render(request, 'examples.html')

def page(request):
    return render(request, 'page.html')

def another_page(request):
    return render(request, 'another_page.html')
"""""