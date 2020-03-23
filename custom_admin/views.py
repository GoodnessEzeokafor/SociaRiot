
from django.shortcuts import (
        render, get_object_or_404,redirect,resolve_url)
from django.http import HttpResponse,HttpResponseRedirect
from  django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.conf import settings
from django.http import HttpResponseRedirect
from .forms import LoginForm,CompanyProfileCreateForm
from django.urls import reverse_lazy, reverse
# Create your views here.
from django.views.generic import (
        ListView,
        DetailView,
        UpdateView,
        DeleteView,
        CreateView,
        View
)
from django.contrib.auth.decorators import login_required
from django.conf import settings
import os
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CompanyProfile



# Create your views here.
class AdminLoginView(LoginView):
    template_name = "account/login.html"
    success_url = reverse_lazy('home')
    form_class=LoginForm

    def get_success_url(self):
        # role = Users.objects.get(membership)
        url = self.get_redirect_url()
        if self.request.user.is_superuser:
            return url or resolve_url(settings.ADMINLOGIN_REDIRECT_URL)
        else:
            return url or resolve_url(settings.LOGIN_REDIRECT_URL)


    def get(self, request,*args, **kwargs):
        if request.user.is_authenticated:
            return HttpResponseRedirect('/')
        else:
            return render(request, self.template_name, self.get_context_data())

class Dashboard(View):
    template_name = "custom_admin/dashboard.html"
    def get(self, request,*args, **kwargs):
        context= {}
        return render(request, self.template_name, {})


class CompanyProfileCreateView(CreateView):
    model = CompanyProfile
    template_name = "custom_admin/profile/create.html"
    form_class=CompanyProfileCreateForm
    # success_url="/account/dashboard/"

    def form_valid(self, form):
        user = User.objects.get(id=self.request.user.id)
        form.instance.user = user
        print("#################################")
        print(form.instance.user)
        print("#################################")
        # form.instance.save()
        form.save()
        return super().form_valid(form)    
    
    def get_success_url(self):
        return reverse("custom_admin:admin_dashboard")


class CompanyProfileDetailView(DetailView):
    model = CompanyProfile
    template_name = "custom_admin/profile/detail.html"
    context_object_name= "profile"
