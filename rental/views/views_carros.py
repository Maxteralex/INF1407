from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.base import View
from rental.forms import AddEditCarroForm
from rental.models import Carro


class ListaCarros(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        carros = Carro.objects.all()
        context = {'carros': carros}
        return render(request, 'rental/listar_carros.html', context)


class AddCarro(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        context = {'form': AddEditCarroForm, 'addedit': 'Adicionar'}
        return render(request, 'rental/addedit_carro.html', context)

    def post(self, request, *args, **kwargs):
        form = AddEditCarroForm(request.POST)
        if form.is_valid():
            carro = form.save()
            carro.save()
            return redirect('listar_carros')
        context = {'form': form, 'addedit': 'Adicionar'}
        return render(request, 'rental/addedit_carro.html', context)


class EditCarro(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=pk)
        form = AddEditCarroForm(instance=carro)
        context = {'form': form, 'addedit': 'Editar'}
        return render(request, 'rental/addedit_carro.html', context)

    def post(self, request, pk, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=pk)
        form = AddEditCarroForm(request.POST, instance=carro)
        if form.is_valid():
            carro = form.save()
            carro.save()
            return redirect('listar_carros')
        context = {'form': form, 'addedit': 'Editar'}
        return render(request, 'rental/addedit_carro.html', context)


class AtivaDesativaCarro(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=pk)
        carro.ativo = not carro.ativo
        carro.save()
        return redirect('listar_carros')
        

class DelCarro(LoginRequiredMixin, View):
    def get(self, request, pk, *args, **kwargs):
        carro = get_object_or_404(Carro, pk=pk)
        carro.delete()
        return redirect('listar_carros')
