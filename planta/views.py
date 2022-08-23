from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse 

#Mensaje tipo cookie temporales 
from django.contrib import messages

#Gestion de errores de base de datos 
from django.db import IntegrityError

from .models import Trabajador,Categoria,Producto,Produccion



# Create your views here.
def index(request):
    return render(request, 'planta/index.html')


def listarTrabajador(request):
    q = Trabajador.objects.all()
    contexto = {'datos': q}

    return render(request, 'planta/trabajador/listar_trabajador.html', contexto)

def formularioTrabajador(request):
    return render(request, 'planta/trabajador/nuevo_trabajador.html')

def guardarTrabajador(request):
    try:
        if request.method == "POST":
            q = Trabajador(cedula = request.POST["cedula"],nombre = request.POST["nombre"],apellido = request.POST["apellido"],correo = request.POST["correo"])
            q.save()

            messages.success(request, "Trabajador guardado exitosamente")
        else:
            messages.warning(request, "No se han enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('planta:listarTrabajador')




    


