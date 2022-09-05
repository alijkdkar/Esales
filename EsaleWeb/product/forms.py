from django import forms



class ProductFullDetail(forms.Form):
    name  = forms.CharField()
    codeNo = forms.CharField()
    description = forms.TextField()
    price = forms.DecimalField(max_digits=8, decimal_places=2)
    active = forms.BooleanField()
    orginal = forms.BooleanField()
    photo = forms.URLField
    
    
