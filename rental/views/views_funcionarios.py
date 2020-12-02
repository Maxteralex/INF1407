from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import Group
from django.http import HttpResponseForbidden
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from rental.forms import AddNovoFuncionarioForm
from rental.models import Solicita, Funcionario, User


class ListaClientesFuncionarios(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        clientes = User.objects.filter(funcionario__isnull=True).all()
        funcionarios = Funcionario.objects.all()
        context = {'clientes': clientes, 'funcionarios': funcionarios, 'form': AddNovoFuncionarioForm}
        return render(request, 'rental/gerenciar_clientes_funcionarios.html', context)


class AddNovoFuncionario(LoginRequiredMixin, View):
    def post(self, request, pk, *args, **kwargs):
        usuario = get_object_or_404(User, pk=pk)
        form = AddNovoFuncionarioForm(request.POST)
        if form.is_valid():
            novo_funcionario = Funcionario(usuario=usuario, salario=form.cleaned_data.get('salario', 0), horas_semana=form.cleaned_data.get('horas_semana', 0))
            novo_funcionario.save()
            grupo_funcionario = Group.objects.filter(name='Funcionario').first()
            if(grupo_funcionario is not None):
                grupo_funcionario.user_set.add(usuario)
        return redirect('gerencia_clientes_funcionarios')


class RemoveFuncionario(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        funcionario = get_object_or_404(Funcionario, pk=pk)
        grupo_funcionario = Group.objects.filter(name='Funcionario').first()
        if(grupo_funcionario is not None):
            grupo_funcionario.user_set.remove(funcionario.usuario)
        funcionario.delete()
        return redirect('gerencia_clientes_funcionarios')
