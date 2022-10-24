
from django.db import models
from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from fac.models import *
from computed_property import ComputedTextField

# Create your models here.
class Bancos(models.Model):
    ID_BANCO = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=100 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class EstadosDep(models.Model):
    ID_ESTADO_DEP = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=50 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Depositos(models.Model):

    ID_DEPOSITO = models.AutoField(primary_key=True, unique=True)
    ID_BANCO = models.ForeignKey(Bancos, on_delete=models.RESTRICT, null=False)
    CUENTA = models.BigIntegerField (null=False, default=0)
    CVE_FOLIO = models.CharField(max_length=240 , default="")
    FECHA_DEPOSITO = models.DateField(blank=True, null=True)
    FECHA_EN_BANCO = models.DateField(blank=True, null=True)
    TIPO_CAMBIO = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    IMPORTE = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    EN_FIRME = models.BooleanField(default=False)
    ID_ESTADO_DEP = models.ForeignKey(EstadosDep, on_delete=models.RESTRICT, null=False)
    ID_RECEPTOR = models.ForeignKey(Ereceptora, on_delete=models.RESTRICT, null=False)
    ID_MONEDA = models.ForeignKey(Monedas, on_delete=models.RESTRICT, null=False)   
    ID_AFILIADO = models.ForeignKey(Afiliado, on_delete=models.RESTRICT, null=True, default=0)
    usuario = UserForeignKey(auto_user_add=True,related_name='+')
    

    # Metadata
    class Meta:
        constraints = [
            UniqueConstraint(fields=["ID_BANCO", "CUENTA","CVE_FOLIO"], name='unique_dep')
        ]

        ordering = ["-FECHA_DEPOSITO"]

    def __str__(self):
        return self.CVE_FOLIO


class Efectivo(models.Model):

    ID_EFECTIVO = models.AutoField(primary_key=True, unique=True)
    FECHA_DEPOSITO = models.DateField(blank=True, null=True)
    IMPORTE = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    PORC_COMI = models.DecimalField(default=0.00, max_digits=5, decimal_places=2)
    IMPORTE_DISP = ComputedTextField(compute_from='_importe_disp')
    SALDO = ComputedTextField(compute_from='_saldo')
    #ID_RECEPTOR = models.ForeignKey(Ereceptora, on_delete=models.RESTRICT, null=False)
    #ID_AFILIADO = models.ForeignKey(Afiliado, on_delete=models.RESTRICT, null=True, default=0)
    usuario = UserForeignKey(auto_user_add=True,related_name='+')

    def _importe_disp(self):
      return self.IMPORTE * self.PORC_COMI / 100

    def _saldo(self):
      return self.IMPORTE_DISP

    # Metadata
    class Meta:
        ordering = ["-FECHA_DEPOSITO"]

    def __str__(self):
        return self.ID_EFECTIVO

    '''
    def save(self, *args, **kwargs):
        super(Efectivo, self).save(*args, **kwargs)
		# Creamos el registro de Caja
        obj, get_or_create = Caja.objects.filter(
                                Q(ID_EFECTIVO=Efectivo.ID_EFECTIVO)
                                ).get_or_create(ID_DEPOSITO      = 0,
                                                ID_EFECTIVO      = Efectivo.ID_EFECTIVO,
                                                IMPORTE          = Efectivo.IMPORTE_DISP,
                                                IMPORTE_DISP     = Efectivo.IMPORTE_DISP,
                                                ID_MONEDA      = 1,
                                                )

'''
