"""This is for login"""
from django import forms
from django.contrib.auth import authenticate, login as django_login
from django.contrib import messages
from reviewers.models import Reviewer


class AuthenticationForm(forms.Form):
    email = forms.EmailField(widget=forms.widgets.TextInput)
    password = forms.CharField(widget=forms.widgets.PasswordInput)


