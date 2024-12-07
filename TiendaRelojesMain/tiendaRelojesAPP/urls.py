from . import views
from django.urls import path
from .views import IndexView, RelojesListView, RelojesView, CompraListView, CompraView, CarritoListView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('relojes', RelojesListView.as_view(), name='relojes'),
    path('detalle/<int:pk>/', RelojesView.as_view(), name='relojDetalle'),
    path('reloj/<int:pk>/detalle_ajax/', views.reloj_detalle_ajax, name='reloj_detalle_ajax'),
    path('compra', CompraListView.as_view(), name='compra'),
    path('compra/detalle/<int:pk>/', CompraView.as_view(), name='compraDetalle'), 
    path('carrito', CarritoListView.as_view(), name='carrito'),

]