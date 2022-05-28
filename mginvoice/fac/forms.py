from django.contrib.admin import forms
from django import forms
from django.core.validators import FileExtensionValidator
from .models import Facturas
import locale

locale.setlocale (locale.LC_ALL, '')

class CargaFacForm(forms.Form):
    docfile = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])],label='')

# *********************************************************
# *********************************************************

class FacturaForm(forms.ModelForm):
    class Meta:
        model = Facturas

        fields = ['ID_EMISOR','FOLIO','SERIE','TIPO_DOCUMENTO',
                    'ID_RECEPTOR',
                    'FECHA_EMISION',
                    'MONEDA',
                    'ESTADO_FACTURA','SUBTOTAL','TOTAL',
                    'IVA','ID_AFILIADO','TIPO_CAMBIO','usuario' ]

        widgets = {
            'ID_EMISOR': forms.Select(attrs={'class': 'form-control', 'label':'Emisor', 'required':False, }),
            'FOLIO': forms.TextInput(attrs={'class': 'form-control'}),
            'SERIE': forms.TextInput(attrs={'class': 'form-control'}),
            'TIPO_DOCUMENTO': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_RECEPTOR': forms.Select(attrs={'class': 'form-control'}),
            'FECHA_EMISION': forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd'}, format='%Y-%m-%d'),
            'MONEDA': forms.TextInput(attrs={'class': 'form-control'}),
            'ESTADO_FACTURA': forms.TextInput(attrs={'class': 'form-control'}),
            'SUBTOTAL': forms.TextInput(attrs={'class': 'form-control'}),
            'TOTAL': forms.TextInput(attrs={'class': 'form-control'}),
            'IVA': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_AFILIADO': forms.Select(attrs={'class': 'form-control'}),
            'TIPO_CAMBIO': forms.TextInput(attrs={'class': 'form-control'}),
            'usuario': forms.Select(attrs={'class': 'form-control'}),
        }
