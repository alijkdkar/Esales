

from django import forms

class UserRegistertionForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserRegistertionForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'

    firstName = forms.CharField()
    lastName = forms.CharField()
    username = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField()
    confirmPassword = forms.CharField()
    #mobile = forms.CharField(max_length=10)



class UserLoginForm(forms.Form):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control'


            
    username =forms.CharField()
    password = forms.CharField()