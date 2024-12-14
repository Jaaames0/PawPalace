from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import *


class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))
    mobilephone = forms.CharField(max_length=12, widget=forms.TextInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2 = forms.CharField(max_length=100, widget=forms.PasswordInput(attrs={'class':'form-control'}))
    username = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class':'form-control'}))

    class Meta:
        model = NewUser
        fields = ('username', 'first_name', 'last_name', 'email', 'mobilephone')





