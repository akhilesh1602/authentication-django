from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


   

def Index(request):
    return render(request, 'main/index.html')


@login_required(login_url='/auth/login')
def sshh(request):
    return HttpResponse('akhilesh')

# before logout.

#@login_required(login_url='/auth/login')
#def Index(request):
   # return HttpResponse('akhilesh')
