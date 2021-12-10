from django.shortcuts import render
from .forms import FormularioContacto

# Create your views here.

def contacto(request):
    data = {
        'form': FormularioContacto()
    }

    if request.method == 'POST':
        formulario = FormularioContacto(data=request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Mensaje Guardado Exitosamente"
        else:
            data["form"] = formulario

    return render(request,"contacto/contacto.html",data)
