# serializers.py
from rest_framework import serializers
from .models import Producto, CategoriaProducto

class CategoriaProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriaProducto
        fields = ['id', 'nombre', 'created', 'updated']

class ProductoSerializer(serializers.ModelSerializer):
    categoria = CategoriaProductoSerializer(read_only=True)  # Para mostrar el nombre de la categoría

    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'imagen', 'disponibilidad', 'categoria', 'created', 'updated']
