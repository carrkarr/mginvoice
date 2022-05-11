from django.contrib.admin import forms
from django import forms
from django.core.validators import FileExtensionValidator

import locale

locale.setlocale (locale.LC_ALL, '')

class CargaFacForm(forms.Form):
    docfile = forms.FileField(allow_empty_file=False,validators=[FileExtensionValidator(allowed_extensions=['csv', 'xls', 'xlsx'])],label='')
