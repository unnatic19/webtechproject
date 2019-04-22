from django import forms

from .models import login

class LoginForm(forms.ModelForm):
    
    class Meta:
        model = login
        fields = ('username', 'password',)

class detail_form(forms.ModelForm):

    class Meta:
        model = login
        fields = ('username', 'password', 'country_name', 'phone_number', 'email',)