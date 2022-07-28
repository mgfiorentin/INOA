# Generated by Django 4.0.6 on 2022-07-28 12:18

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AtivosMonitorados',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ativo', models.CharField(max_length=15, unique=True, verbose_name='Código do ativo')),
                ('tunel_max', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Túnel máx. deve ser maior que R$ 0,00.')], verbose_name='Túnel máx.')),
                ('tunel_min', models.DecimalField(decimal_places=2, max_digits=10, validators=[django.core.validators.MinValueValidator(0, 'Túnel míx. deve ser maior que R$ 0,00.')], verbose_name='Túnel mín.')),
                ('periodicidade', models.IntegerField(validators=[django.core.validators.MinValueValidator(1, 'Periodicidade deve ser maior que 1h')], verbose_name='Periodicidade de atualização [h]')),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='HistoricoPrecos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo_ativo', models.CharField(max_length=15, verbose_name='Código do ativo')),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('data_att', models.DateTimeField(verbose_name='Data de atualização')),
                ('ativo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='InvestimentoApp.ativosmonitorados')),
            ],
        ),
    ]
