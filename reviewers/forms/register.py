"""This is for registration"""
from django import forms
from reviewers.models import Reviewer
from django.forms.extras.widgets import SelectDateWidget
import datetime

class RegistrationForm(forms.ModelForm):
    password1=forms.CharField(widget=forms.widgets.PasswordInput, label='Password')
    password2=forms.CharField(widget=forms.widgets.PasswordInput, label='Confirm Password')

    class Meta:
        this_year = datetime.date.today().year
        yr_choice = []
        for yr in range(1920, int(this_year)):
            yr_choice.append(yr)

        model=Reviewer
        fields=['username', 'email', 'date_of_birth', 'country', 'password1', 'password2']
        widgets={
            'date-of_birth':SelectDateWidget(years=yr_choice)
        }


    def clean_password2(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError("Passwords don't match. Please enter both fields again")
        return self.cleaned_data['password2']

    def save(self, commit=True):
        user=super(RegistrationForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user