from django import forms
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .models import CustomUserModel

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = CustomUserModel
        fields = UserCreationForm.Meta.fields + ('utype','email', 'profile_picture', 'address_line1', 'city', 'state', 'pincode')


class CustomAuthenticationForm(AuthenticationForm):
    username_or_email = forms.CharField(max_length=254, label='Username or Email')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Remove the field not needed based on the context
        if 'username' in self.fields:
            del self.fields['username']
        elif 'email' in self.fields:
            del self.fields['email']

    def clean(self):
        cleaned_data = super().clean()
        username_or_email = cleaned_data.get('username_or_email')
        password = cleaned_data.get('password')

        # Validate either username or email
        if '@' in username_or_email:
            self.cleaned_data['email'] = username_or_email
        else:
            self.cleaned_data['username'] = username_or_email
        return cleaned_data

    class Meta:
        model = CustomUserModel
        fields = ('username_or_email', 'password')

