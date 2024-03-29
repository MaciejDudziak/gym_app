from django import forms
from django.contrib.auth.models import User

class RegisterForm(forms.Form):
    username = forms.CharField(label="username",max_length="150")
    email = forms.EmailField(label="email",max_length="150")
    password = forms.CharField(label="password", widget=forms.PasswordInput())
            
class LogInForm(forms.Form):
    username = forms.CharField(label="username or email address",max_length="150")
    password = forms.CharField(label="password", widget=forms.PasswordInput())