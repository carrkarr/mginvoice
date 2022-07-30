from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(EstadosDep)
#admin.site.register(Monedas)

admin.site.register(Bancos)
admin.site.register(Depositos)

