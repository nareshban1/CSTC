from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('subscription', views.subscription_list, name='subscriptions'),
    path('newsubscription', views.new_subscription, name='newsubscription'),
    path('subscriptiondetail/(<id>)/', views.subscriptionDetail, name='subscriptiondetail'),
    path('report/(<days>)/', views.report, name='report'),
    path('renew/(<id>)/', views.renew, name='renewsubs'),


]