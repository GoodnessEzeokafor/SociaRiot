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
from django.urls import path,include, re_path
from django.contrib.auth.views import (
    LogoutView,
    # PasswordResetView,
    # PasswordResetDoneView,
    # PasswordResetConfirmView,
    # PasswordResetCompleteView
) 
from . import views 
# from custom_admin import views as custom_admin_view

app_name = "account"

urlpatterns = [
    path('login/', views.CustomLoginView.as_view(), name="login"),
    path("logout/", LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("dashboard/profile/create", views.CompanyProfileCreateView.as_view(), name="profile_create")
    # path('dashboard/track/<int:pk>/',views.DashboardTrackDetailView.as_view(), name="track_detail"),
    # # path('dashboard/track/<int:pk>/master',views.master, name="track_master"),
    # re_path('dashboard/track/(?P<username>\w+)/download/$',views.download_mastered_files, name="track_mastered_download"),
    # path('dashboard/payment-customer-info',views.payment_customer_info,name='payment_customer_info'),
    # path('dashboard/support-ticket/add', custom_admin_view.SupportTicketCreateView.as_view(), name="support_ticket_add"),
    # path('dashboard/support-ticket/list', custom_admin_view.SupportTicketListView.as_view(),name="list_ticket"),
    # path('dashboard/support-ticket/<int:pk>/detail', custom_admin_view.SupportDetailView.as_view(),name="detail_ticket"),
    # path('dashboard/mastered/tracks', views.MasteredTracksListView.as_view(),name="mastered_tracks"),

    # path('dashboard/track/<int:pk>/edit', views.MasteringEditTrackView.as_view(), name="track_edit"),
    # path("dashboard/track/<int:pk>/delete", views.MasteringDeleteTrackView.as_view(), name="delete_edit")
]

