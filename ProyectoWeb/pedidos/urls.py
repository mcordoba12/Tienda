from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, LineaPedidoViewSet, historial_compras

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)  # Endpoints para Pedido
router.register(r'lineas-pedido', LineaPedidoViewSet)  # Endpoints para LineaPedido

urlpatterns = [
    path('api/', include(router.urls)),  # Incluye todas las rutas del enrutador
    path('historial/', historial_compras, name='historial_compras'),
]
