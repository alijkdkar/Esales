from typing import List
from django import forms

from EsaleWeb.product.models import ProductDetail



class ProductFullDetail(forms.Form):
    name  = forms.CharField()
    codeNo = forms.CharField()
    description = forms.TextField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    active = forms.BooleanField()
    orginal = forms.BooleanField()
    photo = forms.URLField
    prop = forms.ModelChoiceField(queryset=ProductDetail.objects.filter(), required=False, help_text="ProductDetail")
    
    
