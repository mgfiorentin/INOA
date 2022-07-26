import requests
import json

from django.core.mail import send_mail

from .models import AtivosMonitorados, HistoricoPrecos

from background_task import background


def CarregarEmpresas():
        try:
            url= 'https://api-cotacao-b3.labdo.it/api/empresa/'
            r = requests.get(url)
            lista_empresas = r.json()
        except:
            raise Exception('Erro ao carregar empresa.')
        
        return lista_empresas
    

def CarregarEmpresaById(empresa_id):
        try:
            url= 'https://api-cotacao-b3.labdo.it/api/empresa/%s' %empresa_id 
            r = requests.get(url)
            detalhe_empresa = r.json()
        except:
            raise Exception('Erro ao carregar empresa.')
        
        return detalhe_empresa
    

def CarregarAtivoByCodigo(codigo):
        try:
            url= 'https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/%s' %codigo
            r = requests.get(url)
            ativo = json.loads(r)
        except:
            raise Exception('Erro ao carregar empresa.')
        
        return ativo
    

@background(schedule=0)
def obterCotacaoes(codigo):

    ativo = AtivosMonitorados.objects.get(codigo_ativo=codigo)
    
    url= 'https://api-cotacao-b3.labdo.it/api/cotacao/cd_acao/%s/1' %ativo.codigo_ativo  
    r = requests.get(url)
    cotacao = r.json()

    historico = HistoricoPrecos(codigo_ativo = ativo.codigo_ativo, valor = cotacao[0]['vl_medio'], data_att = cotacao[0]['updated_at'], ativo_id = ativo.id)
    historico.save()
    
    if historico.valor >= ativo.tunel_max:
        mensagem = 'Oportunidade de venda do ativo %s\nTunel configurado: R$ %s\nCotação atual: R$ %s' %(ativo.codigo_ativo, ativo.tunel_max, historico.valor) 
        send_mail(
            subject = 'Oportunidade de venda de ativo!',
            message = mensagem,
            recipient_list = ['matheus.fiorentin@gmail.com',],
            from_email='matheus.fiorentin@gmail.com',
            fail_silently = False
        )
        
    if historico.valor <= ativo.tunel_min:
        mensagem = 'Oportunidade de compra do ativo %s\nTunel configurado: R$ %s\nCotação atual: R$ %s' %(ativo.codigo_ativo, ativo.tunel_min,historico.valor)
        send_mail(
            subject = 'Oportunidade de compra de ativo!',
            message = mensagem,
            recipient_list = ['matheus.fiorentin@gmail.com',],
            from_email='matheus.fiorentin@gmail.com',
            fail_silently = False
        )
       
    return None