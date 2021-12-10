from django.contrib import admin
from django.utils.html import format_html
# Register your models here.

from django.contrib import admin
from .models import Marca,Proveedor,Productos
# Register your models here.

class MarcaAdmin(admin.ModelAdmin):
    list_display=("nombre_marca","created","updated",)
    list_filter = ("nombre_marca",)
    readonly_fields = ('created','updated')

class ProveedorAdmin(admin.ModelAdmin):
    list_display = ("nombre_proveedor","created","updated",)
    readonly_fields = ('created','updated')

class ProductosAdmin(admin.ModelAdmin):
    search_fields = ("id","nombre","precio","cantidad","descripcion","proveedores__nombre_proveedor","marcas__nombre_marca",)
    list_display= ("nombre","descripcion","precio","cantidad","producto_marca","producto_proveedor","imagen",)
    list_filter = ("nombre","marcas__nombre_marca","proveedores__nombre_proveedor",)
    readonly_fields = ('created','updated')

    def producto_marca(self,obj):
        return ", ".join([marc.nombre_marca for marc in obj.marcas.all()])

    def producto_proveedor(self,obj):
        return ", ".join([prov.nombre_proveedor for prov in obj.proveedores.all()])


admin.site.register(Marca,MarcaAdmin)
admin.site.register(Proveedor,ProveedorAdmin)
admin.site.register(Productos,ProductosAdmin)