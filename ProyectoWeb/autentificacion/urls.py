# autentificacion/urls.py
from django.urls import path
from .views import RegistroView, LoginView, LogoutView, LoginPageView, RegistroPageView

app_name = "autentificacion"

urlpatterns = [
    path('api/registro/', RegistroView.as_view(), name='api_registro'),  # Endpoint de API para registro
    path('registro/', RegistroPageView.as_view(), name='registro_page'),  # Página de registro
    path('api/login/', LoginView.as_view(), name='api_login'),  # Endpoint de API para login
    path('api/logout/', LogoutView.as_view(), name='api_logout'),  # Endpoint de API para logout
    path('login/', LoginPageView.as_view(), name='login_page'),  # Página de inicio de sesión
]
