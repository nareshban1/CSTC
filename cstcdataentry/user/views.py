from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User,auth
# Create your views here.
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url='index')
def dashboard(request):
    return render(request, 'home.html')


def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.warning(request, ' Login Failed! Enter the username and password correctly')
            return render(request, 'index.html')
    else:
        return render(request, 'index.html')

def logout(request):
    auth.logout(request)
    return redirect('index')