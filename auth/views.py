from django.shortcuts import render
from auth import forms
# Create your views here.
def login(request):
    loginform = forms.LoginForm()
    context = {
        "form":loginform
    }
    return render(request, 'auth/login.html', context)