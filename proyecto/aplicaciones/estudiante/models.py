from django.db import models
from aplicaciones.tipodocumento.models import TipoDocumento
# Create your models here.

class Estudiante(models.Model):
    name = models.CharField('Nombre', max_length=200)
    email = models.EmailField('Correo Electrónico', max_length=200, default ='averiguar@elcorreo.com')
    idtipodocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    numerodocumento = models.CharField('Nombre', max_length=12)
    
    def __str__(self):
        return self.name
    
   