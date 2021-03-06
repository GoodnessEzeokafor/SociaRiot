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
from . import views 

app_name ="custom_admin"

urlpatterns = [
    path('login', views.AdminLoginView.as_view(), name="admin_login"),
    path('dashboard', views.Dashboard.as_view(),name="admin_dashboard"),
    path("dashboard/<int:pk>/profile", views.CompanyProfileDetailView.as_view(), name="profile_detail"),
    path("dashboard/profile/create", views.CompanyProfileCreateView.as_view(), name="profile_create"),

]


