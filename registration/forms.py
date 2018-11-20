from django import forms
from django.contrib.auth.models import  User
from dashboard.models import Profile
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.ModelForm):
    password=forms.CharField(max_length=50,widget=forms.PasswordInput)

    class Meta:
        model=User
        fields=('username','password','first_name','email',)


class RegistrationForm(forms.ModelForm):
    class Meta:
        model=Profile
        fields=('description',)
