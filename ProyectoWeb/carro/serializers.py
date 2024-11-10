# serializers.py
from rest_framework import serializers
from tienda.models import Producto

class ProductoCarritoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Producto
        fields = ['id', 'nombre', 'precio', 'imagen']

class CarroSerializer(serializers.Serializer):
    producto_id = serializers.IntegerField()
    cantidad = serializers.IntegerField(default=1)
