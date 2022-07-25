from tkinter import CASCADE
from django.db import models

class AtivosMonitorados(models.Model):
    codigo_ativo = models.TextField(max_length=15)
    tunel_max = models.DecimalField(max_digits=10, decimal_places=2)
    tunel_min = models.DecimalField(max_digits=10, decimal_places=2)
    periodicidade = models.IntegerField('Período de att em horas')
    
class HistoricoPrecos(models.Model):
    codigo_ativo = models.TextField(max_length=15)
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    data_att = models.DateTimeField('Data de atualização')
    ativo = models.ForeignKey(AtivosMonitorados, on_delete=models.CASCADE)
    

