from django.urls import path
from rental.views import views_carros, views_solicitacoes, views_funcionarios, views_alugueis

urlpatterns = [
    path('carros/', views_carros.ListaCarros.as_view(), name="listar_carros"),
    path('carros/add/', views_carros.AddCarro.as_view(), name="add_carro"),
    path('carros/edit/<int:pk>/', views_carros.EditCarro.as_view(), name="editar_carro"),
    path('carros/switch_ativo/<int:pk>/', views_carros.AtivaDesativaCarro.as_view(), name="switch_ativo_carro"),
    path('carros/del/<int:pk>/', views_carros.DelCarro.as_view(), name="del_carro"),
    path('credito/', views_solicitacoes.ListaMinhasSolicitacoes.as_view(), name="minhas_solicitacoes"),
    path('credito/gerencia_solicitacoes/', views_solicitacoes.ListaSolicitacoes.as_view(), name="gerencia_solicitacoes"),
    path('credito/cria_solicitacao/', views_solicitacoes.CriaSolicitacao.as_view(), name="criar_solicitacao"),
    path('credito/switch_status_solicitacao/<int:pk>/<str:status>/', views_solicitacoes.MudaStatusSolicitacao.as_view(), name="switch_status_solicitacao"),
    path('funcionarios/', views_funcionarios.ListaClientesFuncionarios.as_view(), name="gerencia_clientes_funcionarios"),
    path('funcionarios/contratar/<int:pk>/', views_funcionarios.AddNovoFuncionario.as_view(), name="contratar_funcionario"),
    path('funcionarios/demitir/<int:pk>/', views_funcionarios.RemoveFuncionario.as_view(), name="demitir_funcionario"),
    path('aluguel/', views_alugueis.ListaMeusAlugueis.as_view(), name="meus_alugueis"),
    path('aluguel/gerenciar/', views_alugueis.ListaAlugueis.as_view(), name="listar_alugueis"),
    path('aluguel/solicita/', views_alugueis.SolicitarAluguel.as_view(), name="solicita_aluguel"),
    path('aluguel/cancela/', views_alugueis.CancelaAluguel.as_view(), name="cancela_aluguel")
]