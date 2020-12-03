from django.db import models
from django.contrib.auth.models import AbstractUser
from datetime import datetime

class User(AbstractUser):
    telefone = models.CharField(max_length=11, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    credito = models.FloatField(default=0)


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    salario = models.FloatField()
    # horas contratadas por semana
    horas_semana = models.IntegerField()


class Carro(models.Model):
    marca = models.CharField(max_length=100)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    preco_base = models.FloatField()
    CONDICOES = ((0, 'Péssima'), (1, 'Ruim'), (2, 'OK'), (3, 'Boa'), (4, 'Semi-novo'), (5, 'Novo'))
    # condição atual do veículo
    condicao = models.IntegerField(choices=CONDICOES)
    # carro ativo é disponibilizado para alugueis, inativos não
    ativo = models.BooleanField(default=True)

    class Meta:
        permissions = (
            ("gerenciar_carros", "Pode criar, ver todos, atualizar, remover e ativar/desativar carros"),
        )


class Aluguel(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_ini = models.DateTimeField()
    data_fim = models.DateTimeField()
    preco_aluguel = models.FloatField()
    CONDICOES = ((0, 'Péssima'), (1, 'Ruim'), (2, 'OK'), (3, 'Boa'), (4, 'Semi-novo'), (5, 'Novo'))
    condicao_antes = models.IntegerField(choices=CONDICOES)
    # só é mudado após avaliação do funcionário
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(blank=True, null=True)
    # só é mudado após a devolução do carro
    data_devolucao = models.DateTimeField(blank=True, null=True)
    taxa_atraso = models.FloatField(blank=True, null=True)
    condicao_depois = models.IntegerField(choices=CONDICOES, blank=True, null=True)


class Solicita(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_solicitacao = models.DateTimeField(default=datetime.now)
    # só é mudado após avaliação de um funcionário
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.CASCADE)
    status = models.BooleanField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(blank=True, null=True)
