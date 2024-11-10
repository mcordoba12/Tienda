from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from tienda.models import Producto
from .carro import Carro
from .serializers import CarroSerializer
from rest_framework.permissions import IsAuthenticated
class AgregarAlCarroView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, producto_id):
        print("Solicitud recibida para agregar al carro")  # Para depuración
        carro = Carro(request)
        try:
            producto = Producto.objects.get(id=producto_id)
            print(f"Producto encontrado: {producto.nombre}")  # Para depuración
            carro.agregar(producto)
            return Response({"message": "Producto agregado al carro"}, status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            print("Producto no encontrado")  # Para depuración
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)

class ObtenerCarroView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        carro = Carro(request)
        items = []
        for key, value in carro.carro.items():
            items.append({
                "producto_id": value["producto_id"],
                "nombre": value["nombre"],
                "cantidad": value["cantidad"],
                "precio": value["precio"],
            })
        return Response({"items": items})


class EliminarProductoView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request, producto_id):
        carro = Carro(request)
        try:
            producto = Producto.objects.get(id=producto_id)
            carro.eliminar(producto=producto)
            return Response({"message": "Producto eliminado del carrito"}, status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class RestarProductoView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, producto_id):
        carro = Carro(request)
        try:
            producto = Producto.objects.get(id=producto_id)
            carro.restar_producto(producto=producto)
            return Response({"message": "Producto restado en el carrito"}, status=status.HTTP_200_OK)
        except Producto.DoesNotExist:
            return Response({"error": "Producto no encontrado"}, status=status.HTTP_404_NOT_FOUND)


class LimpiarCarroView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        carro = Carro(request)
        carro.limpiar_carro()
        return Response({"message": "Carrito limpiado"}, status=status.HTTP_200_OK)

