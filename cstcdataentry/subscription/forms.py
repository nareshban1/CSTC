
from django.forms import TextInput
from django.utils.translation import ugettext_lazy as _
from django import forms
from .models import Subscription, Renew
class newsubscription(forms.ModelForm):
    class Meta:
        model= Subscription
        fields = "__all__"
        widgets = {'ExpiryDate': TextInput(attrs={'readonly': True, }),
                   'InstallDate': TextInput(attrs={'type':'Date', }),
                   'Installation_number': TextInput(attrs={'min':'0', }),
                   'InstallDuration': TextInput(attrs={'min': '0', }),
                   'TotalAmount': TextInput(attrs={'min': '0', }),
                   'AmountReceived': TextInput(attrs={'min': '0', }),
                   'RemainingAmount': TextInput(attrs={'min': '0','readonly': True, })
                   }

class subscriptionUpdate(forms.ModelForm):
    class Meta:
        model= Subscription
        exclude = ['CustomerName']
        labels = {
            'AmountReceived': _('Previously Received'),
        }
        widgets = {
                   'ExpiryDate': TextInput(attrs={'readonly': True, }),
                   'InstallDate': TextInput(attrs={'type':'Date','readonly': True,  }),
                   'Installation_number': TextInput(attrs={'min':'0', 'readonly': True, }),
                   'InstallDuration': TextInput(attrs={'min': '0', 'readonly': True, }),
                   'TotalAmount': TextInput(attrs={'min': '0', 'readonly': True, }),
                   'AmountReceived': TextInput(attrs={'min': '0', 'readonly': True,  }),
                   'RemainingAmount': TextInput(attrs={'min': '0','readonly': True, })
                   }


class renewform(forms.ModelForm):
    class Meta:
        model= Renew
        fields = "__all__"
        exclude = ['Subscription']
        widgets = {'ExpiryDate': TextInput(attrs={'readonly': True, }),
                   'RenewDate': TextInput(attrs={'type': 'Date', }),
                   'InstallDuration': TextInput(attrs={'min': '0', }),
                   'TotalAmount': TextInput(attrs={'min': '0', }),
                   'AmountReceived': TextInput(attrs={'min': '0', }),
                   'RemainingAmount': TextInput(attrs={'min': '0', 'readonly': True, })
                   }
