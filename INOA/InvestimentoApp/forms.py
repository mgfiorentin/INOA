from email.policy import default
from multiprocessing.sharedctypes import Value
from unicodedata import decimal
from django import forms

from .models import AtivosMonitorados

class AtivoForm(forms.ModelForm):
    class Meta:
        model = AtivosMonitorados
        fields = ('codigo_ativo', 'tunel_max', 'tunel_min', 'periodicidade')