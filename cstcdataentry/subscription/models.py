from django.db import models
from customer.models import Customer
from django.core.validators import MaxValueValidator, MinValueValidator
from datetime import datetime, timedelta
# Create your models here.
class Subscription(models.Model):
    CustomerName= models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='customer')
    Installation_number = models.IntegerField(blank=False,default=1, validators=[MinValueValidator(1)])
    InstallDuration= models.IntegerField(blank=False,default=1, validators=[MinValueValidator(1)])
    InstallDate=models.DateField()
    ExpiryDate= models.DateField()
    TotalAmount= models.FloatField(blank=False, default=0, validators=[MinValueValidator(0)])
    AmountReceived=models.FloatField(blank=False,default=0, validators=[MinValueValidator(0)])
    RemainingAmount = models.FloatField(blank=False, default=0, validators=[MinValueValidator(0)])


    def __str__(self):
        return '{}-{}-{}'.format(self.CustomerName.Name, str(self.Installation_number), self.InstallDate)


