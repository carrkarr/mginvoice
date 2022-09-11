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

        fields = ['ID_EMISOR','FOLIO','SERIE','ID_TIPO_DOC',
                    'ID_RECEPTOR',
                    'FECHA_EMISION',
                    'ID_MONEDA',
                    'ID_ESTADO_FAC','SUBTOTAL','TOTAL',
                    'IVA','ID_AFILIADO','TIPO_CAMBIO' ]

        widgets = {
            'ID_EMISOR': forms.Select(attrs={'class': 'form-control', 'label':'Emisor', 'required':True, }),
            'FOLIO': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'SERIE': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'ID_TIPO_DOC': forms.Select(attrs={'class': 'form-control', 'required':True, }),
            'ID_RECEPTOR': forms.Select(attrs={'class': 'form-control', 'required':True,}),
            'FECHA_EMISION': forms.DateInput (attrs={'class': 'date', 'placeholder': 'YYYY-mm-dd'}, format='%Y-%m-%d'),
            'ID_MONEDA': forms.Select(attrs={'class': 'form-control', 'required':True,}),
            'ID_ESTADO_FAC': forms.Select(attrs={'class': 'form-control', 'label':'Edo. Factura.', 'required':True, }),
            'SUBTOTAL': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'TOTAL': forms.TextInput(attrs={'class': 'form-control', 'required':True,}),
            'IVA': forms.TextInput(attrs={'class': 'form-control'}),
            'ID_AFILIADO': forms.Select(attrs={'class': 'form-control'}),
            'TIPO_CAMBIO': forms.TextInput(attrs={'class': 'form-control'}),
            
        }
