from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'description']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'اسم المنتج'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'السعر'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'الوصف', 'rows': 3}),
        }
