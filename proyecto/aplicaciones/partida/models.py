from django.db import models
from aplicaciones.estudiante.models import Estudiante
from aplicaciones.cuenta.models import Cuenta

class Partida(models.Model):
    name = models.CharField('Nota Explicativa', max_length=200)
    idestudiante=models.ForeignKey(Estudiante, on_delete=models.CASCADE, verbose_name="Estudiante")
    idcuenta=models.ForeignKey( Cuenta, on_delete=models.CASCADE, verbose_name="Cuenta")
    idasiento = models.IntegerField(verbose_name='Número de Asiento')
    fecha = models.DateField('Fecha', auto_now=False, auto_now_add=False)
    importe = models.DecimalField('Importe +Debe -Haber)', max_digits=12, decimal_places=2)
   
    def __str__(self):
        return self.name