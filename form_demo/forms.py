from django import forms
from django.forms.fields import BooleanField

# https://docs.djangoproject.com/en/3.2/topics/forms/

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=10)
    your_age = forms.IntegerField(label='Your age')
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField()
    booleanField = forms.BooleanField(required=False)