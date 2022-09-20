from django.urls import path

from . import views

app_name= "planta"
urlpatterns = [
    path('', views.index, name = "index"),
    path ('trabajadores/', views.listarTrabajador, name = "listarTrabajador"),
    path ('formularioTrabajador/', views.formularioTrabajador, name = "formularioTrabajador"),
    path ('guardarTrabajador/', views.guardarTrabajador, name = "guardarTrabajador"),
    path ('productos/', views.listarProducto, name = "listarProducto"),
    path ('formularioProducto/', views.formularioProducto, name = "formularioProducto"),
    path ('guardarProducto/', views.guardarProducto, name = "guardarProducto"),
    path ('formularioEditar/<int:id>', views.formularioEditar, name = "formularioEditar"),
    path ('actualizarProducto/', views.actualizarProducto, name = "actualizarProducto"),
    path ('eliminarProducto/<int:id>', views.eliminarProducto, name = "eliminarProducto"),






]