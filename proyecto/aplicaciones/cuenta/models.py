from django.db import models
from aplicaciones.tipocuenta.models import TipoCuenta
from aplicaciones.estudiante.models import Estudiante
# Create your models here.

class Cuenta(models.Model):
    name = models.CharField('Nombre', max_length=200)
    idtipocuenta=models.ForeignKey( TipoCuenta, on_delete=models.CASCADE, verbose_name="Grupo de Cuentas")
    idestudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
   
    def __str__(self):
        return self.name