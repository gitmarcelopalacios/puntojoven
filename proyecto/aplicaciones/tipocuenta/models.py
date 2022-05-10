from django.db import models

# Create your models here.

class TipoCuenta(models.Model):
    name = models.CharField('Tipo de documento', max_length=100)
    
    def __str__(self):
        return self.name
    
   