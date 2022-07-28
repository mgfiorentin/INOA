from email.policy import default
from multiprocessing.sharedctypes import Value
from unicodedata import decimal
from django import forms

from .models import AtivosMonitorados

class AtivoForm(forms.ModelForm):
    class Meta:
        model = AtivosMonitorados
        fields = ('codigo_ativo', 'tunel_max', 'tunel_min', 'periodicidade', 'email')
        
    def clean(self):
            cleaned_data = super().clean()
            tunel_max = cleaned_data.get("tunel_max")
            tunel_min = cleaned_data.get("tunel_min")

            if tunel_max and tunel_min:
                if tunel_min >= tunel_max:
                    raise forms.ValidationError(
                        'Túnel máximo deve ser maior que mínimo.'
                    )