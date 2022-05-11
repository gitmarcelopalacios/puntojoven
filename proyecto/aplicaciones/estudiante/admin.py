from django.contrib import admin
from .models import Estudiante, TipoDocumento

class EstudianteAdmin(admin.ModelAdmin):
    list_display = (
        "name", 
        "idtipodocumento",
        "numerodocumento",
    )
    
admin.site.register(Estudiante, EstudianteAdmin)


