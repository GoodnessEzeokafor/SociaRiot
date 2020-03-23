from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CompanyProfile


# LOGIN FORM
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control material','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control material','placeholder':'Password'})

class CompanyProfileCreateForm(forms.ModelForm):
    class Meta:
        model = CompanyProfile
        fields = [ 
            # 'user',
                'fullname',
                'profile_pic', 
                'country',
                'company_name',
                'company_address',
                'company_telephone_no'
                ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['fullname'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Full Name'})
        self.fields['company_name'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Company Name'})
        self.fields['company_address'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Company Address'})
        self.fields['company_telephone_no'].widget.attrs.update({'class':'form-control', 'placeholder':'Enter Company Telephone Line'})
        self.fields['profile_pic'].widget.attrs.update({'class':'custom-file-input', 'id':'profilePic'})
        self.fields['country'].widget.attrs.update({'class':'form-control select2', 'width':'Contry'})
