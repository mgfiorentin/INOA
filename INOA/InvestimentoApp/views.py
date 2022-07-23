from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import requests

def index(request):
    return HttpResponse("InvestimentoApp Index")

def lista(request):
    url= 'https://api-cotacao-b3.labdo.it/api/empresa' 
    r = requests.get(url)
    
    lista_empresas = r.json()
    
    template = loader.get_template('investimentoapp/lista.html')
    context = {
        'lista_empresas' : lista_empresas,    
    }
    return HttpResponse(template.render(context,request))

def detalhe(request, empresa_id):
    return HttpResponse("Detalhe empresa %s" %empresa_id)

