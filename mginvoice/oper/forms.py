from django.contrib.admin import forms
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Depositos
import locale

locale.setlocale (locale.LC_ALL, '')

# *********************************************************
# *********************************************************

class DepositoForm(forms.ModelForm):
    class Meta:
        model = Depositos

        fields = [  'ID_BANCO', 'CUENTA', 'CVE_FOLIO', 'FECHA_DEPOSITO',
                    'FECHA_EN_BANCO', 'ID_MONEDA', 'TIPO_CAMBIO',
                    'IMPORTE', 'EN_FIRME', 'ID_ESTADO_DEP', 'ID_RECEPTOR', 'ID_AFILIADO',
                    'usuario' ]

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
            'usuario': forms.Select(attrs={'class': 'form-control', 'required':True,}),
        }
