from django.http import HttpResponseRedirect
from django.shortcuts import render
from .form import newcustomerform
# Create your views here.
from .models import Customer


def customers_list(request):
    obj = Customer.objects.all()
    context ={
        'customers':obj,
    }
    return render(request,'customers.html',context)

def add_customers(request):
    if request.method == 'GET':
        newcustomer_form = newcustomerform()
    else:
        newcustomer_form = newcustomerform(request.POST or None)
        if newcustomer_form.is_valid():
            Name = newcustomer_form.cleaned_data['Name']
            Address1 = newcustomer_form.cleaned_data['Address1']
            Address2 = newcustomer_form.cleaned_data['Address2']
            City = newcustomer_form.cleaned_data['City']
            District = newcustomer_form.cleaned_data['District']
            Zone = newcustomer_form.cleaned_data['Zone']
            PhoneNo = newcustomer_form.cleaned_data['PhoneNo']
            Email = newcustomer_form.cleaned_data['Email']
            Website = newcustomer_form.cleaned_data['Website']
            Contact_Person = newcustomer_form.cleaned_data['Contact_Person']
            Contact_Person_MobileNo = newcustomer_form.cleaned_data['Contact_Person_MobileNo']
            Contact_Person_Email = newcustomer_form.cleaned_data['Contact_Person_Email']
            newcustomer_form.save();
            return HttpResponseRedirect('addcustomers')


    context = {
        'form': newcustomer_form,
    }
    return render(request,'addcustomers.html', context)