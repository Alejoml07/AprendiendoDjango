from datetime import date
from django.db import models

# Create your models here.

class Trabajador(models.Model):
    cedula = models.IntegerField()
    nombre = models.CharField(max_length= 100)
    apellido = models.CharField(max_length= 100)
    correo = models.EmailField(max_length= 250, null=True, blank=True)

    

    def nombreCompleto(self):
        return f"{self.nombre} {self.apellido}"


    def __str__(self):
        return f" {self.nombre} {self.apellido}"


class Categoria(models.Model):
    nombre = models.CharField(max_length=100)
    desc = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return f" {self.nombre}"



class Producto(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    ficha_tecnica= models.TextField()
    costo = models.IntegerField()
    categoria = models.ForeignKey(Categoria,on_delete = models.DO_NOTHING)
    COLOR = (
        ('r','ROJO'),
        ('v','VERDE'),
        ('a','AZUL'),
    )
    color = models.CharField(max_length= 100 ,choices=COLOR, default = 'r')

    
    def __str__(self):
        return f" {self.nombre} "

class Produccion(models.Model):
    trabajador= models.ForeignKey(Trabajador,on_delete= models.DO_NOTHING)
    producto = models.ForeignKey(Producto,on_delete = models.DO_NOTHING)
    cantidad = models.IntegerField()
    fecha = models.DateTimeField()

    def __str__(self):
        return f" {self.trabajador} {self.producto}"






