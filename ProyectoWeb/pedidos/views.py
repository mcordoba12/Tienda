from rest_framework import viewsets
from .models import Pedido, LineaPedido
from .serializers import PedidoSerializer, LineaPedidoSerializer
from rest_framework.permissions import IsAuthenticated
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status

from django.contrib.auth.decorators import login_required


class PedidoViewSet(viewsets.ModelViewSet):
    queryset = Pedido.objects.all()
    serializer_class = PedidoSerializer
    permission_classes = [IsAuthenticated]  # Solo usuarios autenticados

    def create(self, request, *args, **kwargs):
        print("Solicitud POST recibida para crear un pedido")
        print(f"Datos del request: {request.data}")

        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            print("Errores de validación en el serializer:", serializer.errors)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def perform_create(self, serializer):
        # Guarda el pedido y asigna el usuario autenticado
        pedido = serializer.save(user=self.request.user)
        print(f"Pedido creado: {pedido.id}")

        # Crea las líneas de pedido después de crear el pedido
        lineas_pedido_data = self.request.data.get('lineas_pedido', [])
        for linea_data in lineas_pedido_data:
            LineaPedido.objects.create(
                pedido=pedido,
                producto_id=linea_data['producto'],
                cantidad=linea_data['cantidad']
            )

        # Enviar el correo electrónico después de crear las líneas de pedido
        lineas_pedido = pedido.lineas_pedido.all()  # Acceso correcto usando related_name
        enviar_mail(
            pedido=pedido,
            lineas_pedido=lineas_pedido,
            nombreusuario=self.request.user.username,
            email=self.request.user.email
        )



class LineaPedidoViewSet(viewsets.ModelViewSet):
    queryset = LineaPedido.objects.all()
    serializer_class = LineaPedidoSerializer
    permission_classes = [IsAuthenticated]

def enviar_mail(pedido, lineas_pedido, nombreusuario, email):
    asunto = 'Gracias por tu pedido'
    mensaje = render_to_string("emails/pedido.html", {
        "pedido": pedido,  # Pasamos el pedido
        "lineas_pedido": lineas_pedido,  # Pasamos las líneas de pedido
        "nombreusuario": nombreusuario  # Pasamos el nombre del usuario 
    })
    mensaje_texto = strip_tags(mensaje)  # Convierte el mensaje a texto plano
    from_email = 'angela6309gonzalez@gmail.com'  # Cambia por tu correo de origen
    send_mail(asunto, mensaje_texto, from_email, [email], html_message=mensaje)


@login_required
def historial_compras(request):
    # Recuperar los pedidos del usuario autenticado
    pedidos = Pedido.objects.filter(user=request.user).prefetch_related('lineas_pedido__producto').order_by('-created_at')
    return render(request, 'pedidos/historial.html', {'pedidos': pedidos})