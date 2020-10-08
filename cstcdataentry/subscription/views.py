from django.shortcuts import render

# Create your views here.
from subscription.models import Subscription


def subscription_list(request):
    obj = Subscription.objects.all()
    context = {
        'subscriptions': obj,
    }
    return render(request,'subscription.html',context)