from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('customers', views.customers_list, name='customers'),
    path('addcustomers', views.add_customers, name='addcustomers'),
    path('customerupdate/(<id>)/', views.customerUpdate, name='customerupdate'),
    path('customerdetail/(<id>)/', views.customerDetail, name='customerdetail'),


]