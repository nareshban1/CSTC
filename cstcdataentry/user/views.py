from datetime import datetime
from django.db.models import Sum
from django.shortcuts import render
from django.conf import settings
from django.shortcuts import render, HttpResponse, redirect, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from customer.models import Customer
from subscription.models import Subscription,Renew
from django.db.models.functions import ExtractMonth, ExtractYear, TruncMonth
from django.db.models import Count



@login_required(login_url='index')
def dashboard(request):
    subs = Subscription.objects.all()
    customer= Customer.objects.all()
    tusers= Subscription.objects.aggregate(sum=Sum('Installation_number'))['sum'] or 0
    tearned = Renew.objects.aggregate(sum=Sum('AmountReceived'))['sum'] or 0.00
    receive = Renew.objects.aggregate(sum=Sum('RemainingAmount'))['sum'] or 0.00
    today = datetime.now()
    subsMonth  = Subscription.objects.filter(InstallDate__year=today.year).annotate(month = TruncMonth('InstallDate'),).values( 'month')\
        .annotate(total=Count('*')).values('month', 'total').order_by('month')
    userMonth = Subscription.objects.filter(InstallDate__year=today.year).annotate(
        month=TruncMonth('InstallDate'), ).values('month') \
        .annotate(total=Sum('Installation_number')).values('month', 'total').order_by('month')
    currentyear= today.year

    labels = []
    count = []

    for data in subsMonth:
        labels.append(str(data['month'].strftime('%B')))
        count.append(data['total'])

    label = []
    total = []

    for data in userMonth:
        label.append(str(data['month'].strftime('%B')))
        total.append(data['total'])

    context = {
        'subscriptions': subs,
        'customers': customer,
        'totalusers':tusers,
        'totalearned': tearned,
        'receive': receive,
        'subsMonth':userMonth,
        'labels': labels,
        'data': count,
        'label': label,
        'users': total,
        'currentyear':currentyear,

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