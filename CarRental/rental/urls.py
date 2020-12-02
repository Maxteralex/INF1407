from django.urls import path
from rental.views import views_carros

urlpatterns = [
    path('carros/', views_carros.ListaCarros.as_view(), name="listar_carros"),
    path('carros/add/', views_carros.AddCarro.as_view(), name="add_carro"),
    path('carros/edit/<int:pk>/', views_carros.EditCarro.as_view(), name="editar_carro"),
    path('carros/switch_ativo/<int:pk>/', views_carros.AtivaDesativaCarro.as_view(), name="switch_ativo_carro"),
    path('carros/del/<int:pk>/', views_carros.DelCarro.as_view(), name="del_carro"),
    #path('alugar/'),
    #path('credito/'),
]