from django.contrib.auth.models import User
from django.contrib.auth import views
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import render, redirect, reverse
from django.views.generic.base import View
from CarRental.auth.forms import CreateUserForm

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
    def get_success_url(self):
        return reverse('home')

    def get_success_message(self, cleaned_data):
        return 'Bem-vindo ao Car Rental, {}!'.format(self.request.user.first_name if self.request.user.first_name else self.request.user)

class UserLogoutView(views.LogoutView):
    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        messages.add_message(request, messages.SUCCESS, 'Você efetuou logout. Volte sempre!')
        return response
