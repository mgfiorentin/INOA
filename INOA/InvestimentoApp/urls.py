from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('empresas', views.listaEmpresas, name='listaEmpresas'),
    path('empresas/<int:empresa_id>/', views.detalheEmpresa, name='detalheEmpresa'),
    
    path('ativos', views.consultaAtivos, name='consultaAtivos'),
    path('ativos/add', views.addAtivo, name='addAtivo'),
    path('ativos/<int:ativo_id>/edit', views.editAtivo, name='editAtivo'),
    path('ativos/<int:ativo_id>/delete', views.deleteAtivo, name='deleteAtivo'),
    path('ativos/<int:ativo_id>/historico', views.historicoAtivo, name='historicoAtivo'),
    ]