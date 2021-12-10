from django.contrib import admin
# CON EL PUNTO LE INDICAMOS QUE NOS VAMOS A MOVER DENTRO DE ESE DIRECTORIO
# PARA QUE BUSQUE ESE ARCHIVO MODELS
from .models import Servicio

# Register your models here.

class ServicioAdmin(admin.ModelAdmin):
    list_display = ("titulo","contenido","created","updated",)
    readonly_fields = ("created", "updated")

admin.site.register(Servicio, ServicioAdmin)


