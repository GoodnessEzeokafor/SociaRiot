from django import forms 
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm



# LOGIN FORM
class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class':'form-control material','placeholder':'Username'})
        self.fields['password'].widget.attrs.update({'class':'form-control material','placeholder':'Password'})

