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
from CarRental.auth.forms import UserLoginForm


admin.site.site_title = 'Car Rental'
admin.site.site_header = 'Administração Car Rental'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage, name='home'),
    path('about/', views.about, name='about'),
    path('accounts/register/', auth_views.RegisterView.as_view(), name='register'),
    path('accounts/login/', auth_views.UserLoginView.as_view(template_name='auth/login.html', redirect_authenticated_user=True, authentication_form=UserLoginForm), name='login'),
    path('accounts/logout/', auth_views.UserLogoutView.as_view(next_page=reverse_lazy('home')), name='logout'),
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
