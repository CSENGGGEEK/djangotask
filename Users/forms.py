from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUserModel
from django.core.validators import validate_email

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('utype','email' ,'profile_picture', 'address_line1', 'city', 'state', 'pincode')


class CustomAuthenticationForm(AuthenticationForm):
    
    username_email= forms.CharField(max_length=100, label='Username or Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'username' in self.fields:
            del self.fields['username']
        elif 'email' in self.fields:
            del self.fields['email']

    def clean_username_email(self):
        username_or_email = self.cleaned_data.get('username_or_email')
        if validate_email(username_or_email):
            self.cleaned_data['email'] = username_or_email
            del self.cleaned_data['username']

        return None
    
    class Meta:
        model = CustomUserModel
        fields = ('username_email', 'password')

