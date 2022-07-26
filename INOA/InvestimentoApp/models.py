from django.db import models
from django.core.validators import MinValueValidator

class AtivosMonitorados(models.Model):
    codigo_ativo = models.CharField('Código do ativo', 
                                    max_length=15, 
                                    unique=True)
    
    tunel_max = models.DecimalField('Túnel máx.', 
                                    max_digits=10, 
                                    decimal_places=2, 
                                    validators=[MinValueValidator(0.001, 'Túnel máx. deve ser maior que R$ 0,00.')
                                    ])
    
    tunel_min = models.DecimalField('Túnel mín.', 
                                    max_digits=10, 
                                    decimal_places=2, 
                                    validators=[MinValueValidator(0.001, 'Túnel míx. deve ser maior que R$ 0,00.')])
    
    periodicidade = models.IntegerField('Periodicidade de atualização [h]', 
                                        validators=[MinValueValidator(1, 'Periodicidade deve ser no mínimo de 1 hora.')])
    email = models.EmailField(max_length=255)
    
class HistoricoPrecos(models.Model):
    codigo_ativo = models.CharField('Código do ativo', max_length=15)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_att = models.DateTimeField('Data de atualização')
    ativo = models.ForeignKey(AtivosMonitorados, on_delete=models.CASCADE)
    


    