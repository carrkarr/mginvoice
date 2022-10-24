from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from fac.models import *
from oper.models import *


class FormasPago(models.Model):
    ID_FORMA_PAGO = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=30 , unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Repartos(models.Model):

    ID_REPARTO = models.AutoField(primary_key=True, unique=True)
    ID_FACTURA = models.ForeignKey(Facturas, on_delete=models.RESTRICT, null=False,  related_name='reparto_factura')
    TOTAL_FACTURA = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    PORC_RETORNO = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    TOTAL_RETORNO = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    FECHA_REGISTRO = models.DateField(auto_now_add=True)
    FECHA_IMPRESION = models.DateField(blank=True, null=True)
    FECHA_ENTREGA = models.DateField(blank=True, null=True)
    usuario = UserForeignKey(auto_user_add=True,related_name='+')

    # Metadata
    class Meta:
        constraints = [
            UniqueConstraint(fields=["ID_REPARTO", "ID_FACTURA"], name='unique_rep')
        ]

        ordering = ["-FECHA_REGISTRO"]

    def __str__(self):
        return self.ID_REPARTO

class Caja(models.Model):

    ID_CAJA = models.AutoField(primary_key=True, unique=True)
    SERIE = models.CharField(max_length=10 , default="")
    FOLIO = models.CharField(max_length=30 , default="")
    FECHA_DEPOSITO = models.DateField(auto_now_add=True)
    IMPORTE = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    IMPORTE_DISP = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    ID_MONEDA = models.ForeignKey(Monedas, on_delete=models.RESTRICT, null=False)
    usuario = UserForeignKey(auto_user_add=True,related_name='+')

    # Metadata
    class Meta:
        constraints = [
            UniqueConstraint(fields=["SERIE","FOLIO"], name='unique_caja')
        ]

    class Meta:
        ordering = ["-FECHA_DEPOSITO"]

    def __str__(self):
        return self.ID_CAJA






