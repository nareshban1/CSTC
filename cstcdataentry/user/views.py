from django.db.models import Sum
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from subscription.models import Subscription,Renew


@login_required(login_url='index')
def dashboard(request):
    subs = Subscription.objects.all()
    customer= Customer.objects.all()
    tusers= Subscription.objects.aggregate(sum=Sum('Installation_number'))['sum'] or 0
    tearned = Renew.objects.aggregate(sum=Sum('AmountReceived'))['sum'] or 0.00
    receive = Renew.objects.aggregate(sum=Sum('RemainingAmount'))['sum'] or 0.00
    context = {
        'subscriptions': subs,
        'customers': customer,
        'totalusers':tusers,
        'totalearned': tearned,
        'receive': receive,
    }
    return render(request, 'home.html',context)


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