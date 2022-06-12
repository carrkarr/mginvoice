import django_tables2 as tables
from .models import Facturas

class FacHTMxTable(tables.Table):
    class Meta:
        model = Facturas
        template_name = "fac/list_fac.html"