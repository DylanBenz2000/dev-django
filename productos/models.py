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


class Productos(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField()
    cantidad = models.IntegerField()
    descripcion = models.CharField(max_length=250)
    imagen = models.ImageField(upload_to='productos',null=True, blank=True)
    marcas = models.ManyToManyField(Marca)
    proveedores = models.ManyToManyField(Proveedor)

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    
    # CLASE INTERNA
    class Meta:
        verbose_name = 'producto'
        verbose_name_plural = 'productos'

    def __str__(self):
        return self.nombre
