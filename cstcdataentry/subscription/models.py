from django.db import models
from customer.models import Customer
# Create your models here.
class Subscription(models.Model):
    Customer= models.ForeignKey(Customer, on_delete=models.CASCADE)
    Installation_number = models.IntegerField(blank=False,default=0)
    InstallDate=models.DateField(auto_now_add=True)
    ExpiryDate= models.DateField()
    AmountReceived=models.FloatField(blank=False,default=0)
