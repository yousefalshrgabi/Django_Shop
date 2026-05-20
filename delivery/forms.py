from django import forms
from .models import Delivery

class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['name', 'email', 'phone', 'address']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم السائق'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'البريد الإلكتروني'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'رقم الهاتف'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'العنوان', 'rows': 3}),
        }
