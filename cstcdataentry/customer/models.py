from django.db import models

# Create your models here.
class Customer(models.Model):
    Name = models.CharField(max_length=250)
    Address1 = models.CharField(max_length=150)
    Address2 = models.CharField(max_length=150)
    City= models.CharField(max_length=100)
    District = models.CharField(max_length=20)
    Zone = models.CharField(max_length=100)
    PhoneNo= models.CharField(max_length=15)
    Email = models.CharField(max_length=100)
    Website = models.CharField(max_length=100)
    Contact_Person= models.CharField(max_length=100)
    Contact_Person_MobileNo= models.CharField(max_length=15)
    Contact_Person_Email= models.CharField(max_length=100)