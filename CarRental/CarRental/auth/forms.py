from django.core.exceptions import ValidationError
from django import forms
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm, PasswordResetForm, SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.validators import RegexValidator

class CreateUserForm(forms.Form):
    username = forms.CharField(label='Nome de Usuário', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}), validators=[RegexValidator(regex=r'^[A-Za-z\d_]+$', message='Seu usuário deve conter apenas letras, números ou _.')], help_text="150 caracteres ou menos. Letras, números e _ apenas.")
    password1 = forms.CharField(label='Senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), validators=[validate_password], help_text="Sua senha não pode ser muito parecida com o resto das suas informações pessoais. Sua senha precisa conter pelo menos 8 caracteres. Sua senha não pode ser uma senha comumente utilizada. Sua senha não pode ser inteiramente numérica.")
    password2 = forms.CharField(label='Confirmar senha', widget=forms.PasswordInput(attrs={'class': 'form-control'}), help_text="Informe a mesma senha informada anteriormente, para verificação.")
    first_name = forms.CharField(label='Nome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    last_name = forms.CharField(label='Sobrenome', max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label='Email', max_length=254, widget=forms.EmailInput(attrs={'class': 'form-control'}))

    def clean_username(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')

        if len(cleaned_data.get('username')) < 4:
            raise ValidationError('Seu nome de usuário deve ter pelo menos 4 caracteres.')

        if User.objects.filter(username=username).count() > 0:
            raise ValidationError('Este usuário já existe.')

        return username

    def clean_email(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        if User.objects.filter(email=email).count() > 0:
            raise ValidationError('Este email já está associado a um usuário.')

        return email

    def clean(self):
        cleaned_data = super().clean()
        pass1 = cleaned_data.get('password1')
        pass2 = cleaned_data.get('password2')

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