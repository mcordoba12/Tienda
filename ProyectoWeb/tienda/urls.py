from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CategoriaProductoViewSet,tienda

router = DefaultRouter()
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaProductoViewSet)

urlpatterns = [
    path('', include(router.urls)),  # Esto incluye las rutas de tu API
    path('tienda/', tienda, name='Tienda'),  # Asegúrate de que esta ruta esté incluida
]
