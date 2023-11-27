from django.shortcuts import render,redirect
from django.contrib.auth import login as auth_login, authenticate
from django.contrib.auth import logout
from django.http import HttpResponse
from . forms import CustomUserCreationForm,CustomAuthenticationForm

# View to create a form
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return render(request=request,template_name="dashboard.html")
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username_or_email = form.cleaned_data['username_or_email']
            password = form.cleaned_data['password']
            
            # Check if the entered value is an email or username
            if '@' in username_or_email:
                # If it contains '@', consider it as an email
                kwargs = {'email': username_or_email}
            else:
                # Otherwise, consider it as a username
                kwargs = {'username': username_or_email}
            
            user = authenticate(request, **kwargs, password=password)
            
            if user is not None:
                auth_login(request, user)
                return render(request=request, template_name="dashboard.html")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})


def logout(request):
    return render(request, 'logout.html')
