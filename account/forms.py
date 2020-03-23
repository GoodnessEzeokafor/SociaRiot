from django import forms 
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
# from custom_admin.models import PaymentCustomerInfo
from django.contrib.auth.forms import (
    PasswordChangeForm, 
    PasswordResetForm,
    SetPasswordForm
)

from .models import CompanyProfile


class SignupForm(forms.ModelForm):
    username = forms.CharField(max_length=100)
    email = forms.EmailField()
    pwd1 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Password')
    pwd2 = forms.CharField(max_length=50, widget=forms.PasswordInput(), label='Re-Enter Password')
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.fields['username'].widget.attrs.update({
                'class':'form-control material', 
                'placeholder':'Enter Username or Email to log in'
                })
        self.fields['email'].widget.attrs.update({
                'class':'form-control material',
                'placeholder':'Enter Email'
                })
        self.fields['pwd1'].widget.attrs.update({
                'class':'form-control material',
                'placeholder':'Enter Password' 
                })
        self.fields['pwd2'].widget.attrs.update({
            'class':'form-control material',
            'placeholder':'Retype Password' 
            })

    class Meta:
        model = User
        fields = [ 
                'username',
                'email', 
                'pwd1', 
                'pwd2', 
                ]

    def clean_username(self):
        if 'username' in self.cleaned_data:
            try:
                User.objects.get(username=self.cleaned_data['username'])
            except User.DoesNotExist:
                return self.cleaned_data['username']
            else:
                raise forms.ValidationError(
                    'An account with this username already exists')

    def clean_pwd2(self):
        password1 = self.cleaned_data.get("pwd1")
        password2 = self.cleaned_data.get("pwd2")  
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
            user = super().save(commit=False)
            user.set_password(self.cleaned_data['pwd1'])
            if commit:
                user.save()
            return user

        



# LOGIN FORM
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control material','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control material','placeholder':'Password'})



# PASSWORD RESET FORM

class PasswordChangeNewForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['old_password'].widget.attrs.update({'class':'form-control material'})
        self.fields['new_password1'].widget.attrs.update({'class':'form-control material'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control material'})


class PasswordResetNewForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['email'].widget.attrs.update({'class':'form-control material'})


class SetPasswordNewForm(SetPasswordForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['new_password1'].widget.attrs.update({'class':'form-control material', 'placeholder':'Enter New Password'})
        self.fields['new_password2'].widget.attrs.update({'class':'form-control material', 'placeholder':"Confirm New Password"})




#profile
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


