from rest_framework import serializers
from .models import Pedido, LineaPedido

class LineaPedidoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LineaPedido
        fields = ['producto', 'cantidad']

class PedidoSerializer(serializers.ModelSerializer):
    lineas_pedido = LineaPedidoSerializer(many=True)
    user = serializers.ReadOnlyField(source='user.id')  # Establece user como de solo lectura

    class Meta:
        model = Pedido
        fields = ['user', 'created_at', 'lineas_pedido']

    def create(self, validated_data):
        lineas_data = validated_data.pop('lineas_pedido')
        pedido = Pedido.objects.create(**validated_data)
        for linea_data in lineas_data:
            LineaPedido.objects.create(pedido=pedido, **linea_data)
        return pedido
