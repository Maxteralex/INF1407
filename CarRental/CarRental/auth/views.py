from django.contrib.auth.models import User
from django.shortcuts import render, redirect
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
