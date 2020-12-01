from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.views.generic.base import View
from django.shortcuts import render, redirect, reverse
from CarRental.auth.forms import CreateUserForm
from CarRental.settings import EMAIL_HOST_USER as email


class RegisterView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
           return redirect('home')
        context = {
            'form': CreateUserForm()
        }
        return render(request, 'auth/register.html', context)

    def post(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        form = CreateUserForm(request.POST)

        if form.is_valid():
            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password1'],
                email=form.cleaned_data['email'],
                first_name=form.cleaned_data['first_name'],
                last_name=form.cleaned_data['last_name'],
            )
            user.save()
            return redirect('home')

        context = {
            'form': form
        }
        return render(request, 'auth/register.html', context)


class UserLoginView(SuccessMessageMixin, views.LoginView):
    def post(self, request, *args, **kwargs):
        response = super().post(request)
        if response.status_code != 302:
            messages.add_message(self.request, messages.ERROR, 'Nome de usuário ou senha inválidos!')
        return response

    def get_success_url(self):
        return reverse('home')

    def get_success_message(self, cleaned_data):
        return 'Bem-vindo ao Car Rental, {}!'.format(self.request.user.first_name if self.request.user.first_name else self.request.user)


class UserLogoutView(views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, 'Você efetuou logout. Volte sempre!')
        return response


class PasswordResetView(SuccessMessageMixin, views.PasswordResetView):
    def get_success_message(self, cleaned_data):
        return 'Caso este e-mail esteja associado a alguma conta, em alguns instantes você receberá uma mensagem de recuperação de senha.'


class PasswordChangeView(SuccessMessageMixin, views.PasswordChangeView):
    def post(self, request):
        response = super().post(request)

        if response.status_code == 302:
            html_message = render_to_string('auth/password_changed_email.html')
            send_mail(
                subject='[Car Rental] Alteração de Senha Realizada',
                message=strip_tags(html_message),
                from_email=email,
                recipient_list=[request.user.email],
                fail_silently=False
            )

        return response
    
    def get_success_message(self, cleaned_data):
        return 'Pronto! Sua senha foi alterada com sucesso.'


class PasswordResetConfirmView(SuccessMessageMixin, views.PasswordResetConfirmView):
    def get_success_message(self, cleaned_data):
        return 'Pronto! Sua senha foi redefinida.'
