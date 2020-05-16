from django import forms
from .models import Products


class ItemForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'price', 'discount_price', 'category', 'description', 'image']