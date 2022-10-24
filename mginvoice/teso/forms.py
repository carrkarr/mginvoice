from django.contrib.admin import forms
from django import forms
from django.utils.text import slugify
from django.core.validators import FileExtensionValidator
from .models import Repartos
import locale

locale.setlocale (locale.LC_ALL, '')

# *********************************************************
# *********************************************************

class RepartosForm(forms.ModelForm):
    class Meta:
        model = Repartos

        fields = [  'ID_REPARTO', 'ID_FACTURA', 'TOTAL_FACTURA', 'PORC_RETORNO',
                    'TOTAL_RETORNO', 'FECHA_IMPRESION',
                    'FECHA_ENTREGA'
                     ]

        widgets = {
            'ID_FACTURA': forms.Select(attrs={'class': 'form-control', 'label':'Banco', 'required':True, }),
            'TOTAL_FACTURA': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'PORC_RETORNO': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'TOTAL_RETORNO':forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            #'FECHA_REGISTRO':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            'FECHA_IMPRESION':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            'FECHA_ENTREGA':forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd', 'required':True,}, format='%Y-%m-%d'),
            #'usuario': forms.Select(attrs={'class': 'form-control', 'required':True,}),
        }



