from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from rental.forms import CriaSolicitacaoForm
from rental.models import Solicita, Funcionario


class ListaSolicitacoes(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        solicitacoes = Solicita.objects.all()
        context = {'solicitacoes': solicitacoes}
        return render(request, 'rental/listar_solicitacoes.html', context)


class ListaMinhasSolicitacoes(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        solicitacoes = Solicita.objects.filter(cliente=request.user).all()
        form = CriaSolicitacaoForm
        context = {'solicitacoes': solicitacoes, 'private': True, 'form': form}
        return render(request, 'rental/listar_solicitacoes.html', context)


class CriaSolicitacao(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form = CriaSolicitacaoForm(request.POST)
        if form.is_valid():
            solicitacao = Solicita(cliente=request.user, valor=form.cleaned_data.get('valor', 0))
            solicitacao.save()
        return redirect('minhas_solicitacoes')


class MudaStatusSolicitacao(LoginRequiredMixin, View):
    def get(self, request, pk, status, *args, **kwargs):
        funcionario = Funcionario.objects.filter(usuario=request.user).first()
        if funcionario is None:
            return HttpResponseForbidden()
        if status == 'aceita' or status == 'rejeita':
            solicitacao = get_object_or_404(Solicita, pk=pk)
            if status == 'aceita':
                solicitacao.status = True
                solicitacao.cliente.credito += solicitacao.valor
            else:
                solicitacao.status = False
            solicitacao.funcionario = funcionario
            solicitacao.data_avaliacao = datetime.now()
            solicitacao.save()
        return redirect('listar_solicitacoes')
