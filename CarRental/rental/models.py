from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    telefone = models.CharField(max_length=11, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True)
    credito = models.FloatField(default=0)


class Funcionario(models.Model):
    usuario = models.OneToOneField(User, primary_key=True, on_delete=models.CASCADE)
    salario = models.FloatField()
    # horas contratadas por semana
    hh_semana = models.IntegerField()


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
            ("criar_carros", "Pode criar novos carros"),
            ("editar_carros", "Pode atualizar dados de carros"),
            ("deletar_carros", "Pode remover carros ainda não alugados"),
            ("ver_tudo_carros", "Permite ver todas as informações de todos os carros"),
            ("switch_ativo_carros", "Permite ativar ou desativar carros"),
        )


class Aluguel(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_ini = models.DateTimeField()
    data_fim = models.DateTimeField()
    # data de devolução considera que pode ser devolvido adiantado ou atrasado
    data_devolucao = models.DateTimeField(blank=True, null=True)
    preco_aluguel = models.FloatField()
    taxa_atraso = models.FloatField(blank=True, null=True)
    CONDICOES = ((0, 'Péssima'), (1, 'Ruim'), (2, 'OK'), (3, 'Boa'), (4, 'Semi-novo'), (5, 'Novo'))
    condicao_antes = models.IntegerField(choices=CONDICOES)
    condicao_depois = models.IntegerField(choices=CONDICOES, blank=True, null=True)


class Solicita(models.Model):
    cliente = models.ForeignKey(User, on_delete=models.CASCADE)
    valor = models.FloatField()
    data_solicitacao = models.DateTimeField()
    # funcionário que avalia a solicitação
    funcionario = models.ForeignKey(Funcionario, blank=True, null=True, on_delete=models.CASCADE)
    # só é mudado após avaliação do funcionário
    status = models.BooleanField(blank=True, null=True)
    data_avaliacao = models.DateTimeField(blank=True, null=True)
