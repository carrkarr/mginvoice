from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Eemisora)
admin.site.register(Ereceptora)

admin.site.register(Afiliado)
admin.site.register(Facturas)

