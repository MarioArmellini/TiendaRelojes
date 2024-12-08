from . import views
from django.urls import path, include
from .views import IndexView, RelojesListView, RelojesView, CompraListView, CompraView, CarritoListView

from rest_framework.routers import DefaultRouter
from .views import ContactViewSet
# Crea el router para registrar el ViewSet de los contactos
router = DefaultRouter()
router.register(r'contacts', ContactViewSet, basename='contact')

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('relojes', RelojesListView.as_view(), name='relojes'),
    path('detalle/<int:pk>/', RelojesView.as_view(), name='relojDetalle'),
    path('reloj/<int:pk>/detalle_ajax/', views.reloj_detalle_ajax, name='reloj_detalle_ajax'),
    path('compra', CompraListView.as_view(), name='compra'),
    path('compra/detalle/<int:pk>/', CompraView.as_view(), name='compraDetalle'), 
    path('carrito', CarritoListView.as_view(), name='carrito'),

    path('indexVue.html', views.vue_app, name='vue_app'),
    path('api/', include(router.urls)),  # Incluye las rutas de la API
]