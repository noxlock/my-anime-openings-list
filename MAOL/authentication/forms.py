from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import EmailInput, PasswordInput, TextInput
from django.contrib.auth.models import User


class SignupForm(UserCreationForm):
    email = forms.EmailField(widget=EmailInput(attrs={'placeholder':'Email'}))
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password1 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))
    password2 = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Verify Password'}))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput(attrs={'placeholder': 'Username'}))
    password = forms.CharField(widget=PasswordInput(attrs={'placeholder':'Password'}))