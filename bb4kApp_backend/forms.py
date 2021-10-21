from django import forms
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm




class KidRegisterForm(forms.ModelForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ["username", "email", "password", "password"]

class ParentRegisterForm(forms.ModelForm):

    email = forms.EmailField()
    
    class Meta:
        model = User
        fields = ["username", "email", "password", "password"]
