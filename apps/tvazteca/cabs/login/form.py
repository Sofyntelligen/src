from django import forms


class Login(forms.Form):
    inputEmployee = forms.CharField(required=True, max_length=10)
    inputPassword = forms.CharField(required=True)
