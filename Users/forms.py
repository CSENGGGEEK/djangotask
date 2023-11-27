from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('utype','email', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')


class CustomAuthenticationForm(AuthenticationForm):
    username_or_email = forms.CharField(max_length=254, label='Username or Email')
    class Meta:
        model = CustomUserModel
        fields = ('password')
