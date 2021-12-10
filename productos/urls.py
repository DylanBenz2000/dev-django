from django.urls import path
from . import views

urlpatterns = [
    
    
    
    path('', views.productos, name = "Productos"),
    path('marca/<int:marca_id>/',views.marca, name="marca")


]