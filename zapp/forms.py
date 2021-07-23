from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.forms import ModelForm, fields
from django import forms
from django.contrib.auth.models import User



class CreateUser(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']