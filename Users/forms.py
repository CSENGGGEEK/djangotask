from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('utype', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')


class CustomAuthenticationForm(AuthenticationForm):
    class Meta:
        fields = ('username', 'password')

