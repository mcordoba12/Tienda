# views.py
from django.shortcuts import render
from h11 import Response
from rest_framework import viewsets

from carro.carro import Carro
from .models import Producto, CategoriaProducto
from .serializers import ProductoSerializer, CategoriaProductoSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly

class CategoriaProductoViewSet(viewsets.ModelViewSet):
    queryset = CategoriaProducto.objects.all()
    serializer_class = CategoriaProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]  # Solo autenticados pueden modificar

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

def tienda(request):
    productos = Producto.objects.all()  # Obtenemos todos los productos
    return render(request, "tienda/tienda.html", {'productos': productos})  # Renderizamos la plantilla





