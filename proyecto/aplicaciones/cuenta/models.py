from django.db import models
from aplicaciones.tipocuenta.models import TipoCuenta
from aplicaciones.estudiante.models import Estudiante
# Create your models here.

class Cuenta(models.Model):
    name = models.CharField('Nombre', max_length=200)
    idtipodocumento=models.ForeignKey(TipoCuenta, on_delete=models.CASCADE)
    idestudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.name