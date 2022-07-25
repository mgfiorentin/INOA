

from django.shortcuts import render, redirect
from django.template import loader
from django.http import HttpResponse
from django.contrib import messages


from .models import AtivosMonitorados, HistoricoPrecos

from .forms import AtivoForm
from datetime import datetime




from .services import CarregarAtivoByCodigo, CarregarEmpresaById, CarregarEmpresas




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
        return redirect('consultaAtivos')
        
    
    template = loader.get_template('investimentoapp/add.html')
    context = {'form': form
        
    }
    return HttpResponse(template.render(context,request))

def consultaAtivos(request):
    
    ativos = AtivosMonitorados.objects.all()
    
    template = loader.get_template('investimentoapp/monitorados.html')
    context = {
        'ativos': ativos,        
    }
    return HttpResponse(template.render(context,request))
    

def editAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    
    form = AtivoForm(request.POST or None, instance=ativo)
    
    if form.is_valid():
        form.save()
        return redirect('consultaAtivos')

    return render(request, 'investimentoapp/editAtivo.html', {'ativo': ativo, 'form':form})

def deleteAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    
    if request.method == 'POST':
        ativo.delete()
        return redirect ('consultaAtivos')
    
    return render(request, 'investimentoapp/deleteAtivo.html', {'ativo': ativo})

def historicoAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    
    ativo_historico = HistoricoPrecos.objects.filter(codigo_ativo = ativo.codigo_ativo)
    
    
    return render(request, 'investimentoapp/historico.html', {'historico': ativo_historico})




