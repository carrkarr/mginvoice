from decimal import Decimal
from django.db.models import Q
import django_filters
from .models import Facturas

class FacFilter(django_filters.FilterSet):
    querystring = django_filters.CharFilter(method='universal_search',
                                      label="")

    class Meta:
        model = Facturas
        fields = ['querystring']

    def universal_search(self, queryset, FOLIO, value):
        return Facturas.objects.filter(
            Q(FOLIO__icontains=value)
        )