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

# View to login
def login(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            if '@' in username and '.' in username:
                kwargs = {'email':username}
            else:
                kwargs = {'username':username}
            
            user = authenticate(request,**kwargs, password=password)
            if user is not None:
                auth_login(request, user)
                return render(request=request,template_name="dashboard.html")
    else:
        form = CustomAuthenticationForm()

    return render(request, 'login.html', {'form': form})

def logout(request):
    return render(request, 'logout.html')
