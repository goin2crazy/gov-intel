# forms.py
from django import forms
from .models import ComplaintRecord

from django.utils import timezone


class SignInForm(forms.Form):
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'id': 'exampleInputEmail1',
            'aria-describedby': 'emailHelp',
        }),
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            'id': 'exampleInputPassword1',
        }),
    )

class ComplaintRecordForm(forms.ModelForm):
    # You can set the default value for 'datetime' to the current date and time

    class Meta:
        model = ComplaintRecord
        fields = ['text', 'location']
