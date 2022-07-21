from django.db import models
from django.db.models import UniqueConstraint

from django.contrib.auth.models import User
from django.urls import reverse
import django_tables2 as tables

# Create your models here.
class Eemisora(models.Model):
    ID_EMISOR = models.AutoField(primary_key=True, unique=True)
    RFC = models.CharField(max_length=20 , blank=False, unique = True)
    NOMBRE = models.CharField(max_length=240 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Ereceptora(models.Model):
    ID_RECEPTOR = models.AutoField(primary_key=True, unique=True)
    RFC = models.CharField(max_length=20 , blank=False, unique = True)
    NOMBRE = models.CharField(max_length=240 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Afiliado(models.Model):
    ID_AFILIADO = models.AutoField(primary_key=True, unique=True)
    NOMBRE_COMPLETO = models.CharField(max_length=240 , default="")
    NOMBRE_ALIAS = models.CharField(max_length=80 , unique = True)
    COMISION = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    APLICA_A = models.CharField(max_length=40 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE_ALIAS"]

    def __str__(self):
        return self.NOMBRE_ALIAS

class Facturas(models.Model):

    ID_FACTURA = models.AutoField(primary_key=True, unique=True)
    ID_EMISOR = models.ForeignKey(Eemisora, on_delete=models.RESTRICT, null=False)
    FOLIO = models.CharField(max_length=30 , default="")
    SERIE = models.CharField(max_length=10 , default="")
    TIPO_DOCUMENTO = models.CharField(max_length=30 , default="")
    ID_RECEPTOR = models.ForeignKey(Ereceptora, on_delete=models.RESTRICT, null=False)
    FECHA_EMISION = models.DateField(blank=True, null=True)
    MONEDA = models.CharField(max_length=10 , default="")
    ESTADO_FACTURA = models.CharField(max_length=30 , default="")
    SUBTOTAL = models.DecimalField(default=0.00, max_digits=16, decimal_places=2)
    TOTAL = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    IVA = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    ID_AFILIADO = models.ForeignKey(Afiliado, on_delete=models.RESTRICT, null=True, default=0)
    TIPO_CAMBIO = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    
    # Metadata
    class Meta:
        constraints = [
            UniqueConstraint(fields=["ID_EMISOR", "SERIE","FOLIO", "ESTADO_FACTURA"], name='unique_fac')
        ]

        ordering = ["-FECHA_EMISION"]

    def __str__(self):
        return self.FOLIO

    

