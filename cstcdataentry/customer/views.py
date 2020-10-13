from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import newcustomerform,customerupdate
# Create your views here.
from .models import Customer
from subscription.models import Subscription

@login_required(login_url='index')
def customers_list(request):
    obj = Customer.objects.all()
    context ={
        'customers':obj,
    }
    return render(request,'customers.html',context)

@login_required(login_url='index')
def add_customers(request):
    if request.method == 'GET':
        newcustomer_form = newcustomerform()
    else:
        newcustomer_form = newcustomerform(request.POST or None)
        if newcustomer_form.is_valid():
            newcustomer_form.save();
            return HttpResponseRedirect('addcustomers')

    context = {
        'form': newcustomer_form,
    }
    return render(request,'addcustomers.html', context)

@login_required(login_url='index')
def customerDetail(request, id):
    customer= Customer.objects.get(id=id)
    subscription = Subscription.objects.all()
    subscriptions = subscription.filter(CustomerName_id = id)
    context = {
        'customer': customer,
        'subscription':subscriptions,
    }
    return render(request, 'customersdetails.html', context)


@login_required(login_url='index')
def customerUpdate(request,id):
    cus = Customer.objects.get(id=id)
    if request.method == 'GET':
        customer_update= customerupdate(instance=cus)
    else:
        customer_update = customerupdate(request.POST,instance= cus)
        if customer_update.is_valid():
            customer_update.save()
            return HttpResponseRedirect('/customerdetail/('+id+')')



    context = {
        'form': customer_update,
        'sub':cus,
    }
    return render(request,'updatecustomers.html', context)