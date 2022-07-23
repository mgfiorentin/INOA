
from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse

from .models import AtivosMonitorados, HistoricoPrecos

from .forms import AtivoForm
from datetime import datetime

from .services import CarregarAtivoByCodigo, CarregarEmpresaById, CarregarEmpresas


import json


def index(request):
    return HttpResponse("InvestimentoApp Index")

def lista(request):
    lista_empresas = CarregarEmpresas();
    template = loader.get_template('investimentoapp/lista.html')
    context = {
        'lista_empresas' : lista_empresas,    
    }
    return HttpResponse(template.render(context,request))

def detalhe(request, empresa_id):
    
    detalhe_empresa = CarregarEmpresaById(empresa_id)
    
        
    template = loader.get_template('investimentoapp/detalhe.html')
    context = {
        'detalhe_empresa': detalhe_empresa,        
    }
    return HttpResponse(template.render(context,request))
    
def addAtivo(request):
    
    form = AtivoForm(request.POST or None)
    
    if form.is_valid():
        ativo_aux=form.cleaned_data['codigo_ativo']
        tunel_max_aux=form.cleaned_data['tunel_max']
        tunel_min_aux=form.cleaned_data['tunel_min']
        periodicidade_aux=form.cleaned_data['periodicidade']

        
        ativo = AtivosMonitorados(codigo_ativo = ativo_aux,tunel_max = tunel_max_aux,tunel_min=tunel_min_aux,periodicidade=periodicidade_aux)
        ativo.save()      
        return redirect('lista')
        
    
    
    template = loader.get_template('investimentoapp/add.html')
    context = {'form': form
        
    }
    return HttpResponse(template.render(context,request))

def consultaAtivos(request):
    
    return HttpResponse("Consulta de ativos")