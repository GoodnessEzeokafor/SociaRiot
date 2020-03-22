"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include 
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
) 
from account.forms import (
    PasswordChangeNewForm, PasswordResetNewForm,SetPasswordNewForm
)
from . import views 
urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include('account.urls')),
    path('', views.HomeView.as_view(), name="home"),
    path('about', views.AboutView.as_view(), name="about"),
    path('contact', views.ContactView.as_view(), name="contact"),
    path('service', views.ServiceView.as_view(), name="service"),
    path('password_reset/',PasswordResetView.as_view(template_name="account/password_reset_form.html", form_class=PasswordResetNewForm), name="password_reset"),
    path('password_reset/done/',PasswordResetDoneView.as_view(template_name="account/password_reset_email_done.html"), name="password_reset_done"),
    path("reset/<uidb64>/<token>/",PasswordResetConfirmView.as_view(template_name="account/password_reset_confirm.html", form_class=SetPasswordNewForm), name="password_reset_confirm"),
    path("reset/done/", PasswordResetCompleteView.as_view(template_name="account/password_reset_done.html"), name="password_reset_complete"),

]
