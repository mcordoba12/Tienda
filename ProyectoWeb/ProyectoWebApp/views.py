# views.py
from django.shortcuts import render
from carro.carro import Carro

def home(request):   
    carro = Carro(request)  # Instanciamos la clase Carro (si se requiere en el backend)
    return render(request, "ProyectoWebApp/home.html")  # Renderizamos la plantilla home.html
