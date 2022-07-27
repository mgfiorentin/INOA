# InvestimentoApp - Desafio técnico INOA
### Projeto desenvolvido baseado nos requisitos funcionais do desafio técnico.

# 

# Instruções de instalação
## Tecnologias e frameworks
Projeto desenvolvido em Python v3.10.5 + Django v.4.0.6. Instruções de instalação disponíveis nos links:

https://docs.djangoproject.com/en/3.1/topics/install/#install-python

https://docs.djangoproject.com/en/4.0/topics/install/

## Bibliotecas
`django4-background-tasks`

`django-filter`

# Pastas e arquivos relevantes

`/INOA` contém arquivos do projeto 'INOA', enquanto `INOA/InvestimentoApp` contém o app 'InvestimentoApp';

`InvestimentoApp/migrations` contém as migrações do banco de dados geradas pelo Django;

`InvestimentoApp/templates` contém os arquivos de template HTML; 

`filters.py` contém modelos da biblioteca 'django-filter' para realizar buscas no banco de dados;

`forms.py` contém os formulários Django;

`models.py` contém os modelos armazenados em banco de dados e suas relações;

`urls.py` contém todas as URLs da aplicação;

`views.py` contém todos os métodos relacionados às URLs;

## Configurações
O envio de e-mails de notificações de compra/venda deve ser configurado, fornecendo um endereço e senha válida no arquivo `settings.py`. A autenticação via Gmail requer a configuração de uma "senha de aplicativos" nas configurações do seu provedor.

Altere as seguintes linhas com suas informações de remetente:

`EMAIL_HOST_USER = 'yourAppEmail@gmail.com'`

`EMAIL_HOST_PASSWORD = 'yourAppPassword'`

`DEFAULT_FROM_EMAIL = 'yourAppEmail@gmail.com'`


# URLs
A URL base da aplicação é

- `host:port/investimento`

A visualização, criação, configuração e exclusão de ativos monitorados são feitas a partir das URLs 
- Visualizar: `host:port/investimento/ativos`
- Monitorar novo ativo: `host:port/investimento/ativos/add`
- Editar configuração: `host:port/investimento/ativos/{id}/edit`
- Excluir monitoramento: `host:port/investimento/ativos/{id}/delete`
- Buscar: `host:port/investimento/ativos/busca`
- Visualizar histórico de cotações do ativo: `host:port/investimento/ativos/{id}/historico`

Onde {id} significa a identificação de registro no banco de dados.


A aplicação também permite consultar todas as empresas com ativos cadastrados na B3 a partir das URLs
- Lista de empresas: `host:port/investimento/empresas`
- Detalhes da empresa: `host:port/investimento/empresas/{id}`
