from django.urls import path
from .views import (
    AgregarAlCarroView,
    EliminarProductoView,
    RestarProductoView,
    LimpiarCarroView,
    ObtenerCarroView,
)

app_name = "carro"

urlpatterns = [
    path('api/carro/agregar/<int:producto_id>/', AgregarAlCarroView.as_view(), name='agregar_al_carro'),
    path('api/carro/eliminar/<int:producto_id>/', EliminarProductoView.as_view(), name='eliminar'),
    path('api/carro/restar/<int:producto_id>/', RestarProductoView.as_view(), name='restar'),
    path('api/carro/limpiar/', LimpiarCarroView.as_view(), name='limpiar'),
path('api/carro/', ObtenerCarroView.as_view(), name='obtener_carro')
]
