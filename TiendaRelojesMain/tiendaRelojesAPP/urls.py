from django.urls import path
from . import views
from django.urls import path
from .views import IndexView, RelojesListView, RelojesView, CompraListView, CompraView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('relojes', RelojesListView.as_view(), name='relojes'),
    path('relojes/detalle/<int:pk>/', RelojesView.as_view(), name='relojDetalle'),
    path('compra', CompraListView.as_view(), name='compra'),
    path('compra/detalle/<int:pk>/', CompraView.as_view(), name='compraDetalle'), 
]