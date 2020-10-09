from django import forms
from .models import Customer
class newcustomerform(forms.ModelForm):
    class Meta:
        model= Customer
        fields = ["Name","Address1","Address2","City","District","Zone","PhoneNo","Email","Website","Contact_Person","Contact_Person_MobileNo","Contact_Person_Email"]