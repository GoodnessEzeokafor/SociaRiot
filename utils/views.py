from django.shortcuts import render

# Create your views here.



def page_not_found(request,exception):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'main/404.html',values_for_template,status=404)

def server_error(request):
    # Dict to pass to template, data could come from DB query
    values_for_template = {}
    return render(request,'main/500.html',values_for_template,status=500)
