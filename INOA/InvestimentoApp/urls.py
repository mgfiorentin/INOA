from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lista', views.lista, name='lista'),
    path('<int:empresa_id>/', views.detalhe, name='detalhe'),
    path('add', views.addAtivo, name='addAtivo'),
    path('monitorados', views.consultaAtivos, name='consultaAtivos'),
    path('<int:ativo_id>/edit', views.editAtivo, name='editAtivo'),
    path('<int:ativo_id>/delete', views.deleteAtivo, name='deleteAtivo'),
    path('<int:ativo_id>/historico', views.historicoAtivo, name='historicoAtivo'),
    
]