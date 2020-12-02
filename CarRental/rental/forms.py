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

