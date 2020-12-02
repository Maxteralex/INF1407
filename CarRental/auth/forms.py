from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator
from rental.models import User

class CreateUserForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário*', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[RegexValidator(regex=r'^[A-Za-z\d_]+$', message='Seu usuário deve conter apenas letras, números ou _.')], help_text="Pelo menos 4 caracteres e no máximo 150. Letras, números e _ apenas.")
    password1 = forms.CharField(label='Senha*', widget=forms.PasswordInput(attrs={'class': 'form-control'}), validators=[validate_password], help_text="Sua senha não pode ser muito parecida com o resto das suas informações pessoais. Sua senha precisa conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente utilizada. Sua senha não pode ser inteiramente numérica.")
    password2 = forms.CharField(label='Confirmar senha*', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="Informe a mesma senha informada anteriormente, para verificação.")
    first_name = forms.CharField(label='Nome*', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome*', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email*', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(label='CPF*', min_length=11, max_length=11, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[RegexValidator(regex=r'^\d{11}$', message='O CPF deve conter 11 caracteres numéricos.')], help_text="Apenas os números do CPF.")
    telefone = forms.CharField(label='Telefone', required=False, max_length=12, min_length=8, validators=[RegexValidator(regex=r'^(\d{8,12})?$', message='Todos os caracteres devem ser numéricos.')], widget=forms.TextInput(attrs={'class': 'form-control'}), help_text="Deve ser composto apenas por números (espaços apenas ilustrativos): DDD NNNNN NNNN")

    def clean_username(self):
        username = self.cleaned_data.get('username')

        if len(self.cleaned_data.get('username')) < 4:
            raise ValidationError('Seu nome de usuário deve ter pelo menos 4 caracteres.')

        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Este usuário já existe.')

        return username

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise ValidationError('Este email já está associado a um usuário.')

        return email
    
    def clean_cpf(self):
        cpf = self.cleaned_data.get('cpf')
        # Testa por CPF duplicado
        if User.objects.filter(cpf=cpf).all():
            raise ValidationError('Já há um usuário com esse CPF.')
        # Verifica CPFs inválidos com todos os dígitos repetidos (ex.: 00000000000)
        for i in range(10):
            temp = ''.join(str(i) for j in range(11))
            if cpf == temp:
                raise ValidationError('Esse não é um CPF válido.')
        # Verifica CPFs inválidos pelo algoritmo de validação de CPF
        soma = 0
        # Primeiro dígito verificador
        for i in range(9):
            soma += (10-i)*int(cpf[i])
        soma = (soma*10)%11
        if soma == 10:
            soma = 0
        if soma != int(cpf[9]):
            raise ValidationError('Esse não é um CPF válido.')
        # Segundo dígito verificador
        soma = 0
        for i in range(10):
            soma += (11-i)*int(cpf[i])
        soma = (soma*10)%11
        if soma == 10:
            soma = 0
        if soma != int(cpf[10]):
            raise ValidationError('Esse não é um CPF válido.')
        
        return cpf

    def clean(self):
        pass1 = self.cleaned_data.get('password1')
        pass2 = self.cleaned_data.get('password2')

        if pass1 is not None and pass1 != pass2:
            self.add_error('password2', 'As senhas não correspondem.')


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.CharField(label='Usuário', widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomPasswordChangeForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordChangeForm, self).__init__(*args, **kwargs)

    old_password = forms.CharField(label='Antiga senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password1 = forms.CharField(label='Nova senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    new_password2 = forms.CharField(label='Confirmar nova senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}))


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class CustomPasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(CustomPasswordResetForm, self).__init__(*args, **kwargs)

    email = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))


class CustomSetPasswordForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super(CustomSetPasswordForm, self).__init__(*args, **kwargs)

    new_password1 = forms.CharField(label="Nova senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="Sua senha não pode ser muito parecida com o resto das suas informações pessoais. Sua senha precisa conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente utilizada. Sua senha não pode ser inteiramente numérica.")
    new_password2 = forms.CharField(label="Confirmar nova senha", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
