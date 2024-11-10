from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # Administración
    path('admin/', admin.site.urls),

    # Aplicaciones del Proyecto
    path('tienda/', include('tienda.urls')),  # Rutas de la app Tienda
    path('carro/', include('carro.urls')),    
    path('autentificacion/', include('autentificacion.urls')),  # Rutas de autenticación
    path('pedidos/', include('pedidos.urls')),  # Rutas de Pedidos

    # Página Principal
    path('', include('ProyectoWebApp.urls')),  # Rutas de la app principal
]


# Servir archivos de medios en modo de desarrollo
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
