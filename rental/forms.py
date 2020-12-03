from django import forms
from rental.models import Carro


class AddEditCarroForm(forms.ModelForm):
    class Meta:
        model = Carro
        fields = ['marca', 'modelo', 'ano', 'preco_base', 'condicao']
        labels = {
            'preco_base': 'Preço Base',
            'condicao': 'Condição atual'
        }
        widgets = {
            'marca': forms.TextInput(attrs={'class': 'form-control'}),
            'modelo': forms.TextInput(attrs={'class': 'form-control'}),
            'ano': forms.NumberInput(attrs={'class': 'form-control'}),
            'preco_base': forms.NumberInput(attrs={'class': 'form-control'}),
            'condicao': forms.Select(attrs={'class': 'form-control'}),
        }


class CriaSolicitacaoForm(forms.Form):
    valor = forms.FloatField(label="Valor Solicitado", widget=forms.NumberInput(attrs={'class': 'form-control'}))


class AddNovoFuncionarioForm(forms.Form):
    salario = forms.FloatField(label="Salário", widget=forms.NumberInput(attrs={'class': 'form-control'}))
    horas_semana = forms.IntegerField(label="Horas Contratadas por Semana", widget=forms.NumberInput(attrs={'class': 'form-control'}))


class SolicitaAluguelForm(forms.Form):
    carro = forms.IntegerField(widget=forms.HiddenInput())
    data_ini = forms.DateTimeField()
    data_fim = forms.DateTimeField()