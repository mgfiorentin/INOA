import requests
import json

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
    