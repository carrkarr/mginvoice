from django.db import models
from django.db.models import UniqueConstraint

from django.contrib.auth.models import User
from django_userforeignkey.models.fields import UserForeignKey
from django.urls import reverse

#from teso.views import create_reparto

# Create your models here.
class Eemisora(models.Model):
    ID_EMISOR = models.AutoField(primary_key=True, unique=True)
    RFC = models.CharField(max_length=20 , unique=True)
    NOMBRE = models.CharField(max_length=240 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.RFC

class Ereceptora(models.Model):
    ID_RECEPTOR = models.AutoField(primary_key=True, unique=True)
    RFC = models.CharField(max_length=20 , unique=True)
    NOMBRE = models.CharField(max_length=240 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.RFC

class Afiliado(models.Model):
    ID_AFILIADO = models.AutoField(primary_key=True, unique=True)
    NOMBRE_COMPLETO = models.CharField(max_length=240 , default="")
    NOMBRE_ALIAS = models.CharField(max_length=80 , unique=True)
    COMISION = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    APLICA_A = models.CharField(max_length=40 , default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE_ALIAS"]

    def __str__(self):
        return self.NOMBRE_ALIAS

class EstadosFac(models.Model):
    ID_ESTADO_FAC = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=30 , unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class EdosFacRet(models.Model):
    ID_ESTADO_RET = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=30 , unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class TiposDoc(models.Model):
    ID_TIPO_DOC = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=30 , unique=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Monedas(models.Model):
    ID_MONEDA = models.AutoField(primary_key=True, unique=True)
    NOMBRE = models.CharField(max_length=9 , unique=True, default="")
    usuario = models.ForeignKey(User, on_delete=models.CASCADE,)

    # Metadata
    class Meta:
        ordering = ["NOMBRE"]

    def __str__(self):
        return self.NOMBRE

class Facturas(models.Model):

    ID_FACTURA = models.AutoField(primary_key=True, unique=True)
    ID_EMISOR = models.ForeignKey(Eemisora, on_delete=models.RESTRICT, null=False)
    FOLIO = models.CharField(max_length=30 , default="")
    SERIE = models.CharField(max_length=10 , default="")
    ID_RECEPTOR = models.ForeignKey(Ereceptora, on_delete=models.RESTRICT, null=True)
    FECHA_EMISION = models.DateField(blank=True, null=True)
    ID_MONEDA = models.ForeignKey(Monedas, on_delete=models.RESTRICT, null=True)
    ID_ESTADO_FAC = models.ForeignKey(EstadosFac, on_delete=models.RESTRICT, null=True)
    ID_ESTADO_RET = models.ForeignKey(EdosFacRet, on_delete=models.RESTRICT, null=True)
    SUBTOTAL = models.DecimalField(default=0.00, max_digits=16, decimal_places=2)
    TOTAL = models.DecimalField(default=0.00, max_digits=19, decimal_places=2)
    IVA = models.DecimalField(default=0.00, max_digits=12, decimal_places=2)
    ID_AFILIADO = models.ForeignKey(Afiliado, on_delete=models.RESTRICT, null=True, default=0)
    ID_TIPO_DOC = models.ForeignKey(TiposDoc, on_delete=models.RESTRICT, null=True, default='')
    TIPO_CAMBIO = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    usuario = UserForeignKey(auto_user_add=True,related_name='+')
    FECHA_REGISTRO = models.DateField(auto_now_add=True)

    # Metadata
    class Meta:
        constraints = [
            UniqueConstraint(fields=["ID_EMISOR", "SERIE","FOLIO"], name='unique_fac')
        ]

        ordering = ["-FECHA_EMISION"]

    def get_absolute_url(self):
        return reverse('create-reparto', kwargs={'pk': self.pk})

    def __str__(self):
        return self.FOLIO


