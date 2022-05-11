from django.contrib import admin
from .models import Cuenta
from .models import Estudiante, TipoCuenta


class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "idtipocuenta",
        "idestudiante",
    )
    ordering = ("idestudiante",)
    
admin.site.register(Cuenta, EstudianteAdmin)

