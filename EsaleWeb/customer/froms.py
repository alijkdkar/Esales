

from django import forms

class UserRegistertionForm(forms.Form):
    firstName = forms.CharField()
    lastName = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    #mobile = forms.CharField(max_length=10)



class UserLoginForm(forms.Form):
    username =forms.CharField()
    password = forms.CharField()