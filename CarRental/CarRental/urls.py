"""CarRental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include, reverse_lazy

from CarRental import views
from CarRental.auth import views as auth_views
from CarRental.auth.forms import UserLoginForm, CustomPasswordResetForm, CustomPasswordChangeForm, CustomSetPasswordForm
from CarRental.settings import EMAIL_HOST_USER as email



admin.site.site_title = 'Car Rental'
admin.site.site_header = 'Administração Car Rental'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/register/', auth_views.RegisterView.as_view(), name='register'),
    path('accounts/login/', auth_views.UserLoginView.as_view(
        template_name='auth/login.html',
        redirect_authenticated_user=True,
        authentication_form=UserLoginForm
    ), name='login'),
    path('accounts/logout/', auth_views.UserLogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        form_class=CustomPasswordResetForm,
        template_name='auth/password_reset_form.html',
        success_url=reverse_lazy('home'),
        from_email=email,
        subject_template_name='auth/password_reset_subject.txt',
        email_template_name='auth/password_reset_email.html',
    ), name='password_reset'),
    path('accounts/password_change/', auth_views.PasswordChangeView.as_view(
        template_name='auth/password_change_form.html',
        form_class=CustomPasswordChangeForm,
        success_url=reverse_lazy('home')
    ), name='password_change'),
    path('accounts/password_reset/', auth_views.PasswordResetView.as_view(
        template_name='auth/password_reset_form.html',
        form_class=CustomPasswordResetForm,
        success_url=reverse_lazy('home')
    ), name='password_reset'),
    path('accounts/reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        success_url=reverse_lazy('home'),
        form_class=CustomSetPasswordForm,
        template_name='auth/password_reset_confirm.html'
    ), name='password_reset_confirm'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
