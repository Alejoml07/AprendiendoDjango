from django.urls import path

from . import views

app_name= "planta"
urlpatterns = [
    path('', views.index, name = "index"),
    path ('trabajadores/', views.listarTrabajador, name = "listarTrabajador"),
    path ('formularioTrabajador/', views.formularioTrabajador, name = "formularioTrabajador"),
    path ('guardarTrabajador/', views.guardarTrabajador, name = "guardarTrabajador")


]