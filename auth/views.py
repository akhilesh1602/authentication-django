from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth import authenticate
from auth import forms
from django.contrib.auth.views import LoginView, LogoutView

class Login(LoginView):
    template_name = 'auth/login.html'
    redirect_authenticated_user = True

class Logout(LogoutView):
    pass


# Create your views here.
def login(request):
    loginform = forms.LoginForm()
    error = None

    if request.method == 'POST':
        loginForm = forms.LoginForm(request.POST)
        if loginForm.is_valid():
            username = loginForm.cleaned_data['username']
            password = loginForm.cleaned_data['password']
            user = authenticate(username = username, password = password)
            if user:
                return HttpResponseRedirect('/')
            else:
                error = "invalid username or password"
    context = {
        "form":loginform,
        "error":error
    }
    return render(request, 'auth/login.html', context)