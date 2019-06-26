from django import forms
from app_5_g.models import models_data
from django.contrib.auth.models import User
class user_forms(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())
    class Meta():
        model=User
        fields=('username','password',)
class profile_forms(forms.ModelForm):
    class Meta():
        model=models_data
        fields=('profile_pic',)
