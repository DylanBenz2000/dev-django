from django.shortcuts import render
from productos.models import Productos,Marca
# Create your views here.

def productos(request):
    
    products = Productos.objects.all()
    return render(request,"productos/productos.html",{"products": products})

def marca(request,marca_id):
    marca=Marca.objects.get(id=marca_id)
    products = Productos.objects.filter(marcas=marca)
    return render(request,"productos/marca.html",{'marca':marca,"products": products})
