from django.db import models

# Create your models here.

class Marca(models.Model):
    nombre_marca = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # CLASE INTERNA
    class Meta:
        verbose_name = 'marca'
        verbose_name_plural = 'marcas'

    def __str__(self):
        return self.nombre_marca


class Proveedor(models.Model):
    nombre_proveedor = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    # CLASE INTERNA
    class Meta:
        verbose_name = 'proveedor'
        verbose_name_plural = 'proveedores'

    def __str__(self):
        return self.nombre_proveedor


class Productos_Inventarios(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    descripcion = models.CharField(max_length=250)
    cantidad = models.IntegerField()


    marcas = models.ManyToManyField(Marca)
    proveedores = models.ManyToManyField(Proveedor)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    # CLASE INTERNA
    class Meta:
        verbose_name = 'producto_inventario'
        verbose_name_plural = 'productos_inventarios'

    def __str__(self):
        return self.nombre