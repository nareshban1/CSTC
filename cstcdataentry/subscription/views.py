import datetime
import csv
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .forms import newsubscription, subscriptionUpdate, renewform
from .models import Subscription, Renew
# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None


@login_required(login_url='index')
def subscription_list(request):
    obj = Subscription.objects.all()
    days = None
    expiryfilter = request.GET.get('expiryfilter')

    if is_valid_queryparam(expiryfilter):
        days = int(expiryfilter)
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=days)
        obj = obj.filter(ExpiryDate__range=[start_date, end_date])

    context = {
        'subscriptions': obj,
        'days':days,
    }
    return render(request,'subscription.html',context)


@login_required(login_url='index')
def report(request,days):
    obj = Subscription.objects.all()
    if is_valid_queryparam(days) and days != "None":
        output = []
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="expiry.csv"'
        writer = csv.writer(response)
        day = int(days)
        start_date = datetime.date.today()
        end_date = start_date + datetime.timedelta(days=day)
        obj = obj.filter(ExpiryDate__range=[start_date, end_date])
        query_set = obj
        # Header
        writer.writerow(
            ['Subscription ID', 'Company Name', 'Client ID', 'No Of Installation', 'Install Date', 'Expiry Date'])
        for subscription in query_set:
            output.append([subscription.id, subscription.CustomerName, subscription.CustomerName.id,
                             subscription.Installation_number, subscription.InstallDate, subscription.ExpiryDate])
         # CSV Data
        writer.writerows(output)
        return response
    else:
        return HttpResponseRedirect('/subscription')

@login_required(login_url='index')
def new_subscription(request):

    if request.method == 'GET':
        newsubscription_form = newsubscription()
    else:
        newsubscription_form = newsubscription(request.POST or None)
        if newsubscription_form.is_valid():
            n=newsubscription_form.save()
            ren = Renew()
            ren.Subscription=Subscription.objects.get(id=n.pk)
            ren.RenewDate = newsubscription_form.cleaned_data['InstallDate']
            ren.ExpiryDate = newsubscription_form.cleaned_data['ExpiryDate']
            ren.TotalAmount = newsubscription_form.cleaned_data['TotalAmount']
            ren.RemainingAmount = newsubscription_form.cleaned_data['RemainingAmount']
            ren.AmountReceived = newsubscription_form.cleaned_data['AmountReceived']
            ren.InstallDuration = newsubscription_form.cleaned_data['InstallDuration']
            ren.save()
            return HttpResponseRedirect('/subscription')



    context = {
        'form': newsubscription_form,
    }
    return render(request,'newsubscription.html', context)

@login_required(login_url='index')
def subscriptionDetail(request,id):
    sub = Subscription.objects.get(id=id)
    ren = Renew.objects.filter(Subscription=id).order_by('-id')
    renu= Renew.objects.filter(Subscription=id).latest('id')
    if request.method == 'GET':
        subscription_update= subscriptionUpdate(instance= sub)
    else:
        subscription_update = subscriptionUpdate(request.POST,instance= sub)
        if subscription_update.is_valid():
            subscription_update.save()
            renu.RemainingAmount = subscription_update.cleaned_data['RemainingAmount']
            renu.AmountReceived = subscription_update.cleaned_data['AmountReceived']
            renu.save()
            return render(request,'subscriptiondetail.html', {'form': subscription_update,'sub':sub, 'renews':ren,})



    context = {
        'form': subscription_update,
        'sub':sub,
        'renews':ren,
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