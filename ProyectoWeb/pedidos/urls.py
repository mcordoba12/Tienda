from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PedidoViewSet, LineaPedidoViewSet

router = DefaultRouter()
router.register(r'pedidos', PedidoViewSet)  # Endpoints para Pedido
router.register(r'lineas-pedido', LineaPedidoViewSet)  # Endpoints para LineaPedido

urlpatterns = [
    path('api/', include(router.urls)),  # Incluye todas las rutas del enrutador
]
