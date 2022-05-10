from django.db import models
from aplicaciones.tipocuenta.models import TipoCuenta
# Create your models here.

class Cuenta(models.Model):
    name = models.CharField('Nombre', max_length=200)
    idtipodocumento=models.ForeignKey(TipoDocumento, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name