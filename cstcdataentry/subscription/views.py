from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import newsubscription, subscriptionUpdate, renewform
from .models import Subscription
# Create your views here.

@login_required(login_url='index')
def subscription_list(request):
    obj = Subscription.objects.all()

    context = {
        'subscriptions': obj,
    }
    return render(request,'subscription.html',context)

@login_required(login_url='index')
def new_subscription(request):

    if request.method == 'GET':
        newsubscription_form = newsubscription()
    else:
        newsubscription_form = newsubscription(request.POST or None)
        if newsubscription_form.is_valid():
            newsubscription_form.save()
            return HttpResponseRedirect('/subscription')



    context = {
        'form': newsubscription_form,
    }
    return render(request,'newsubscription.html', context)

@login_required(login_url='index')
def subscriptionDetail(request,id):
    sub = Subscription.objects.get(id=id)
    if request.method == 'GET':
        subscription_update= subscriptionUpdate(instance= sub)
    else:
        subscription_update = subscriptionUpdate(request.POST,instance= sub)
        if subscription_update.is_valid():
            subscription_update.save()
            return render(request,'subscriptiondetail.html', {'form': subscription_update,'sub':sub,})



    context = {
        'form': subscription_update,
        'sub':sub,
    }
    return render(request,'subscriptiondetail.html', context)



@login_required(login_url='index')
def renew(request,id):
    sub = Subscription.objects.get(id=id)
    if request.method == 'GET':
        renew_form = renewform()
    else:
        renew_form =renewform(request.POST)
        if renew_form.is_valid():

           sub.ExpiryDate=renew_form.cleaned_data['ExpiryDate']
           sub.TotalAmount = renew_form.cleaned_data['TotalAmount']
           sub.RemainingAmount = renew_form.cleaned_data['RemainingAmount']
           sub.AmountReceived=renew_form.cleaned_data['AmountReceived']
           sub.InstallDuration = renew_form.cleaned_data['InstallDuration']
           renew_form.save()
           sub.save();
           return HttpResponseRedirect('/subscription')

    context = {
        'form': renew_form,
        'sub':sub,
    }
    return render(request,'renew.html', context)