from django import forms
from django.forms import ChoiceField

from .models import Customer

ZONES=(
    ("Mechi", "Mechi"),
    ("Koshi", "Koshi"),
    ("Sagarmatha", "Sagarmatha"),
    ("Janakpur", "Janakpur"),
    ("Bagmati", "Bagmati"),
    ("Narayani", "Narayani"),
    ("Gandaki", "Gandaki"),
    ("Lumbini", "Lumbini"),
    ("Dhaulagiri", "Dhaulagiri"),
    ("Rapti", "Rapti"),
    ("Karnali", "Karnali"),
    ("Bheri", "Bheri"),
    ("Seti", "Seti"),
    ("Mahakali", "Mahakali"),

)

DISTRICTS =(
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Bajura", "Bajura"),
    ("Banke", "Banke"),
    ("Bara", "Bara"),
    ("Bardiya", "Bardiya"),
    ("Bhaktapur", "Bhaktapur"),
    ("Bhojpur", "Bhojpur"),
    ("Chitwan", "Chitwan"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),
    ("Achham", "Achham"),
    ("Arghakhanchi", "Arghakhanchi"),
    ("Baglung", "Baglung"),
    ("Baitadi", "Baitadi"),
    ("Bajhang", "Bajhang"),

)
class newcustomerform(forms.ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"
        widgets = {'Zone': forms.Select(choices = ZONES),
                   'District': forms.Select(choices = DISTRICTS),
                   }


class customerupdate(forms.ModelForm):
    class Meta:
        model= Customer
        fields = "__all__"
        widgets = {'Zone': forms.Select(choices=ZONES),
                   'District': forms.Select(choices=DISTRICTS),
                   }

