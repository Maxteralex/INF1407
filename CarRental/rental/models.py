from django.db import models


class Cliente(models.Model):
    usuario = models.OneToOneField('User', primary_key=True, on_delete=models.CASCADE)
    telefone = models.CharField(max_length=15, required=False)
    cpf = models.CharField(max_length=11)
    credito = models.FloatField(default=0)


class Funcionario(models.Model):
    usuario = models.OneToOneField('User', primary_key=True, on_delete=models.CASCADE)
    salario = models.FloatField()
    cpf = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
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


class Aluguel(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    carro = models.ForeignKey(Carro, on_delete=models.CASCADE)
    data_ini = models.DateTimeField()
    data_fim = models.DateTimeField()
    # data de devolução considera que pode ser devolvido adiantado ou atrasado
    data_devolucao = models.DateTimeField(required=False)
    preco_aluguel = models.FloatField()
    taxa_atraso = models.FloatField(required=False)
    CONDICOES = ((0, 'Péssima'), (1, 'Ruim'), (2, 'OK'), (3, 'Boa'), (4, 'Semi-novo'), (5, 'Novo'))
    condicao_antes = models.IntegerField(choices=CONDICOES)
    condicao_depois = models.IntegerField(choices=CONDICOES, required=False)
