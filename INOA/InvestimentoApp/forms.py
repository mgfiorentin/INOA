from email.policy import default
from multiprocessing.sharedctypes import Value
from unicodedata import decimal
from django import forms



class AtivoForm(forms.Form):
    codigo_ativo = forms.CharField(label='Código do ativo', max_length=20)
    tunel_max = forms.DecimalField(max_digits=10, decimal_places=2)
    tunel_min = forms.DecimalField(max_digits=10, decimal_places=2)
    periodicidade =forms.IntegerField()