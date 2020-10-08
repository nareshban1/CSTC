from django.shortcuts import render

# Create your views here.
from customer.models import Customer


def customers_list(request):
    obj = Customer.objects.all()
    context ={
        'customers':obj,
    }
    return render(request,'customers.html',context)