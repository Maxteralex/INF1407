from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from rental.forms import SolicitaAluguelForm
from rental.models import Aluguel, Carro, Funcionario


class ListaAlugueis(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        alugueis = Aluguel.objects.order_by("-data_ini").all()
        context = {'alugueis': alugueis}
        return render(request, 'rental/listar_alugueis.html', context)


class ListaMeusAlugueis(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        solicitacoes = Aluguel.objects.filter(cliente=request.user).all()
        context = {'alugueis': solicitacoes, 'private': True}
        return render(request, 'rental/listar_alugueis.html', context)


class SolicitarAluguel(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        form = SolicitaAluguelForm
        context = {'form': form}
        return render(request, 'rental/solicita_aluguel.html', context)

    def post(self, request, *args, **kwargs):
        form = SolicitaAluguelForm(request.POST)
        if form.is_valid():
            #alugueis = Aluguel(cliente=request.user, valor=form.cleaned_data.get('valor', 0))
            #alugueis.save()
            return redirect('meus_alugueis')
        return render(request, 'rental/solicita_aluguel.html', context)


# Função que a partir de uma marca responde com os modelos referentes a essa marca
def getMarcaModelos():
    pass


# Função que a partir dos modelos de carro dá opções de carros
def getCarros():
    pass


class MudaStatusAluguel(LoginRequiredMixin, View):
    def get(self, request, pk, status, *args, **kwargs):
        funcionario = Funcionario.objects.filter(usuario=request.user).first()
        if funcionario is None:
            return HttpResponseForbidden()
        if status == 'aceita' or status == 'rejeita':
            aluguel = get_object_or_404(Aluguel, pk=pk)
            if status == 'aceita':
                aluguel.status = True
                aluguel.cliente.credito -= aluguel.preco_aluguel * (aluguel.data_ini - aluguel.data_fim).days
                aluguel.cliente.save()
            else:
                aluguel.status = False
            aluguel.funcionario = funcionario
            aluguel.data_avaliacao = datetime.now()
            aluguel.save()
        return redirect('listar_alugueis')


class CancelaAluguel(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        aluguel = get_object_or_404(Aluguel, pk=pk)
        if aluguel.status is None and request.user == aluguel.cliente:
            carro.delete()
        return redirect('listar_carros')