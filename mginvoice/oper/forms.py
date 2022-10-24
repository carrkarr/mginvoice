from django.contrib.admin import forms
from django import forms
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from .models import Depositos, Efectivo
import locale

locale.setlocale (locale.LC_ALL, '')

# *********************************************************
# *********************************************************

class DepositosForm(forms.ModelForm):
    class Meta:
        model = Depositos

        fields = [  'ID_BANCO', 'CUENTA', 'CVE_FOLIO', 'FECHA_DEPOSITO',
                    'FECHA_EN_BANCO', 'ID_MONEDA', 'TIPO_CAMBIO',
                    'IMPORTE', 'EN_FIRME', 'ID_ESTADO_DEP', 'ID_RECEPTOR', 'ID_AFILIADO'
                     ]

        widgets = {
            'ID_BANCO': forms.Select(attrs={'class': 'form-control', 'label':'Banco', 'required':True, }),
            'CUENTA': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'CVE_FOLIO': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'FECHA_DEPOSITO':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            'FECHA_EN_BANCO':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            'MONEDA': forms.Select(attrs={'class': 'form-control', 'label':'Moneda', 'required':True, }),
            'TIPO_CAMBIO': forms.TextInput (attrs={'class': 'form-control'}),
            'IMPORTE': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'EN_FIRME': forms.CheckboxInput (attrs={'class': 'form-control', 'label':'En Firme?'}),
            'ID_ESTADO_DEP': forms.Select(attrs={'class': 'form-control', 'label':'ESTADO', 'required':True,}),
            'ID_RECEPTOR': forms.Select(attrs={'class': 'form-control', 'label':'RECEPTOR', 'required':True,}),
            'ID_AFILIADO': forms.Select(attrs={'class': 'form-control', 'label':'AFILIADO', 'required':True,}),
            #'usuario': forms.Select(attrs={'class': 'form-control', 'required':True,}),
        }


# Create your models here.

    def clean_name(self) -> str:
        name: str = self.cleaned_data["CVE_FOLIO"]
        if Depositos.objects.filter(CVE_FOLIO=name).exclude(id=self.instance.id).exists():
            raise forms.ValidationError(f"Un Deposito con el mismo {name} exists")
        return name

    def save(self, commit: bool = True) -> Depositos:
        task: Depositos = super().save(commit)
        task.save()
        return task


class EfectivoForm(forms.ModelForm):
    class Meta:
        model = Efectivo

        fields = [  'ID_EFECTIVO', 'FECHA_DEPOSITO', 'IMPORTE', 'PORC_COMI',
                    #'IMPORTE_DISP', 'SALDO', 
                     ]

        widgets = {
            'ID_EFECTIVO': forms.Select(attrs={'class': 'form-control', 'label':'Efectivo', 'required':True, }),
            'FECHA_DEPOSITO':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            'IMPORTE': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'PORC_COMI': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            #'IMPORTE_DISP': forms.TextInput(attrs={'class': 'form-control', 'readonly':True,}),
            #'SALDO': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            #'usuario': forms.Select(attrs={'class': 'form-control', 'required':True,}),
        }


# Create your models here.

    def save(self, commit: bool = True) -> Efectivo:
        task: Efectivo = super().save(commit)
        task.save()
        return task
