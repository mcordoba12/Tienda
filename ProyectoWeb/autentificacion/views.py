from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from django.contrib.auth import login, logout, authenticate
from .serializers import RegistroSerializer
from django.contrib.auth.models import User
from django.views.generic import TemplateView

class RegistroView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = RegistroSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()  # Guarda el usuario
            login(request, user)  # Loguea al usuario automáticamente
            return Response({"message": "Usuario registrado correctamente"}, status=status.HTTP_201_CREATED)
        print(serializer.errors)  # Para ver errores en la consola del servidor
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # Obtiene los datos del formulario
        username = request.data.get('username')  # Cambiado a request.data
        password = request.data.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return Response({"message": "Inicio de sesión exitoso"}, status=status.HTTP_200_OK)
        return Response({"error": "Credenciales inválidas"}, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    def post(self, request):
        logout(request)
        return Response({"message": "Cierre de sesión exitoso"}, status=status.HTTP_200_OK)

class LoginPageView(TemplateView):
    template_name = 'login/login.html'

class RegistroPageView(TemplateView):
    template_name = 'registro/registro.html'
