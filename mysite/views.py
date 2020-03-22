from django.views.generic import TemplateView




class HomeView(TemplateView):
    template_name  = "main/home.html"


class AboutView(TemplateView):
    template_name  = "main/about.html"
    

class ContactView(TemplateView):
    template_name  = "main/contact.html"
    

class ServiceView(TemplateView):
    template_name  = "main/service.html"



# def bad_request(request):
#     # Dict to pass to template, data could come from DB query
#     values_for_template = {}
#     return render(request,'400.html',values_for_template,status=400)
# def permission_denied(request):
#     # Dict to pass to template, data could come from DB query
#     values_for_template = {}
#     return render(request,'403.html',values_for_template,status=403)