from django.contrib import admin

from .models import Trabajador,Categoria,Producto,Produccion

# Register your models here.
@admin.register(Trabajador)
class TrabajadorAdmin(admin.ModelAdmin):
    list_display = ("id",'cedula','nombre','apellido','correo', 'nombreCompleto',) 
    search_fields = ['nombre','id']

    

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'ficha_tecnica', 'costo', 'categoria', 'color','descripcionCategoria')
    search_fields = ['nombre','categoria__nombre']
    list_filter = ['categoria'] 
    #list_editable = ['color','categoria']

    def descripcionCategoria(self,obj):
        return obj.categoria.nombre


@admin.register(Produccion)
class ProduccionAdmin(admin.ModelAdmin):
    list_display = ('trabajador', 'producto', 'cantidad', 'fecha', )



@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'desc', )

