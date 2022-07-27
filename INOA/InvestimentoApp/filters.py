
import django_filters

from .models import AtivosMonitorados

class AtivosFilter(django_filters.FilterSet):
    class Meta:
        model = AtivosMonitorados
        fields = ['codigo_ativo']