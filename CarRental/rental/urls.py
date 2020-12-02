from django.urls import path
from rental.views import views_carros, views_solicitacoes

urlpatterns = [
    path('carros/', views_carros.ListaCarros.as_view(), name="listar_carros"),
    path('carros/add/', views_carros.AddCarro.as_view(), name="add_carro"),
    path('carros/edit/<int:pk>/', views_carros.EditCarro.as_view(), name="editar_carro"),
    path('carros/switch_ativo/<int:pk>/', views_carros.AtivaDesativaCarro.as_view(), name="switch_ativo_carro"),
    path('carros/del/<int:pk>/', views_carros.DelCarro.as_view(), name="del_carro"),
    path('credito/', views_solicitacoes.ListaMinhasSolicitacoes.as_view(), name="minhas_solicitacoes"),
    path('credito/gerencia_solicitacoes/', views_solicitacoes.ListaSolicitacoes.as_view(), name="gerencia_solicitacoes"),
    path('credito/cria_solicitacao/', views_solicitacoes.CriaSolicitacao.as_view(), name="criar_solicitacao"),
    path('credito/switch_status_solicitacao/<int:pk>/<str:status>/', views_solicitacoes.MudaStatusSolicitacao.as_view(), name="switch_status_solicitacao")
    #path('funcionarios/', views_funcionarios.ListaUsuarios.as_view(), name="lista_usuarios")
    #path('alugar/', views_aluguel.ListaAlugueis, name="listar_alugueis"),
    
]