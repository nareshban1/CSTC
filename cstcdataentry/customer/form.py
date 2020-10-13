from django import forms
from .models import Customer
class newcustomerform(forms.ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"



class customerupdate(forms.ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"

