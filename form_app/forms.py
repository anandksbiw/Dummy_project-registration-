from django import forms
from django.contrib.auth.models import User
from  . import  models



class UserProfileInfoForm(forms.ModelForm):

    class Meta():
        model = models.UserProfileInfo
        fields = ('user','name','address','profile_pic','resume')


# class UserForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput())
#
#     class Meta():
#         model = User
#         fields = ('username','email','password')
#
