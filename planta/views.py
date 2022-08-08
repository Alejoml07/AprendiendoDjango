from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def saludar(request):
    return HttpResponse("Hola <strong> mundo </strong>! <a href='/planta/'/> Regresar </a>")

def index(request):
    return render(request, 'planta/index.html')

def saludoEspecial(request,dato):
    return HttpResponse(f"hola {dato}")

def multiplicacion(request,num):
    return HttpResponse(f"hola {num*2}")

def suma(request,sum1,sum2):
    return HttpResponse(f"Resultado de {sum1} + {sum2} = {sum1 + sum2}")

def loginFormulario(request):
    return render(request, 'planta/login/login-form.html')

def login(request):
    u = request.POST["usuario"]
    c = request.POST["clave"]

    if u == "admin" and c == "1234":
        return HttpResponse ("Bienvenido!!")    
    else:
        return HttpResponse("Contraseña incorrecta...")

def sumaFormulario(request):
    return render(request, 'planta/login/suma.html')

def sumar(request):
    num1= int(request.POST["numero1"])
    num2 = int(request.POST["numero2"])
    r = int(num1) + int(num2)
    return HttpResponse (f"Resultado de {num1} + {num2} = {r}")

    


