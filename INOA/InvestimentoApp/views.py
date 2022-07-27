from django.shortcuts import render, redirect
from django.http import HttpResponse

from .models import AtivosMonitorados, HistoricoPrecos
from .forms import AtivoForm
from .services import CarregarEmpresaById, CarregarEmpresas, obterCotacaoes

from background_task.models import CompletedTask, Task

def index(request):
       
    return render(request, 'investimentoapp/index.html')

def lista(request):
    lista_empresas = CarregarEmpresas();

    return render(request, 'investimentoapp/lista.html', {'lista_empresas': lista_empresas})

def detalhe(request, empresa_id):
    detalhe_empresa = CarregarEmpresaById(empresa_id)
    
    return render(request, 'investimentoapp/detalhe.html', {'detalhe_empresa': detalhe_empresa})

def addAtivo(request):
    
    form = AtivoForm(request.POST or None)
    
    if form.is_valid():
        form.save()      
        ativo = form.cleaned_data['codigo_ativo']
        periodicidade_sec = form.cleaned_data['periodicidade']*60*60
        
        obterCotacaoes(ativo, repeat=periodicidade_sec, repeat_until=None, verbose_name='%s'%ativo)

        return redirect('consultaAtivos')
        
    return render(request, 'investimentoapp/add.html', {'form': form})

def consultaAtivos(request):

    ativos = AtivosMonitorados.objects.all()
    
    return render(request, 'investimentoapp/monitorados.html', {'ativos': ativos})

def editAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    
    form = AtivoForm(request.POST or None, instance=ativo)
    
    if form.is_valid():
        form.save()
        
        Task.objects.get(verbose_name = ativo.codigo_ativo).delete()
        CompletedTask.objects.get(verbose_name = ativo.codigo_ativo).delete()
        
        ativo = form.cleaned_data['codigo_ativo']
        periodicidade_sec = form.cleaned_data['periodicidade']*60*60
        obterCotacaoes(ativo, repeat=periodicidade_sec, repeat_until=None, verbose_name='%s'%ativo)
        
        return redirect('consultaAtivos')

    return render(request, 'investimentoapp/editAtivo.html', {'ativo': ativo, 'form':form})

def deleteAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    
    if request.method == 'POST':
        ativo.delete()
        Task.objects.get(verbose_name = ativo.codigo_ativo).delete()
        CompletedTask.objects.get(verbose_name = ativo.codigo_ativo).delete()
        return redirect ('consultaAtivos')
    
    return render(request, 'investimentoapp/deleteAtivo.html', {'ativo': ativo})

def historicoAtivo(request, ativo_id):
    
    ativo = AtivosMonitorados.objects.get(id=ativo_id)
    ativo_historico = HistoricoPrecos.objects.filter(codigo_ativo = ativo.codigo_ativo)
    
    return render(request, 'investimentoapp/historico.html', {'historico': ativo_historico})




