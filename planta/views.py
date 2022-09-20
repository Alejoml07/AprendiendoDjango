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

def listarProducto(request):
    q = Producto.objects.all()
    contexto = {'datos': q}

    return render(request, 'planta/producto/listar_producto.html', contexto)

def formularioProducto(request):
    q = Categoria.objects.all()
    contexto = {"cat":q}
    return render(request, 'planta/producto/nuevo_producto.html',contexto)


def guardarProducto(request):
    try:
        if request.method == "POST":
            
            q = Producto(nombre = request.POST["nombre"],
                         ficha_tecnica = request.POST["ficha_tecnica"],
                         costo = request.POST["costo"],
                         categoria = Categoria.objects.get(pk = request.POST["categoria"]),
                         color = request.POST["color"])
            q.save()

            messages.success(request, "Producto guardado exitosamente")
        else:
            messages.warning(request, "No se han enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('planta:listarProducto')

def formularioEditar(request,id):
    p = Producto.objects.get( pk = id )
    q = Categoria.objects.all()
    contexto = {"cat":q, "producto":p}
    return render(request, 'planta/producto/editar_producto.html',contexto)

def actualizarProducto(request):
    try:
        if request.method == "POST":
            p = Producto.objects.get(pk = request.POST["id"])
            c = Categoria.objects.get(pk = request.POST["categoria"])
            
            
            p.nombre = request.POST["nombre"]
            p.ficha_tecnica = request.POST["ficha_tecnica"]
            p.costo = request.POST["costo"]
            p.categoria = c
            p.color = request.POST["color"]
            p.save()

            messages.success(request, "Producto guardado exitosamente")
        else:
            messages.warning(request, "No se han enviado datos...")

    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('planta:listarProducto')

def eliminarProducto(request, id):
    try:
        p = Producto.objects.get(pk = id)
        p.delete()
        messages.success(request, "Producto eliminado exitosamente")
    except IntegrityError:
        messages.warning(request, "No se puede eliminar ya que hay otros productos relacionados...")
    except Exception as e:
        messages.error(request, f"Error: {e}")
    
    return redirect('planta:listarProducto')

        


        



    


