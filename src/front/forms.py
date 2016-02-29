from django import forms
from captcha.fields import ReCaptchaField


class ContactsForm(forms.Form):
    name = forms.CharField(label="* Your name", max_length=100, widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(label="* Email", max_length=200, widget=forms.TextInput(attrs={'class': 'form-control'}))
    text = forms.CharField(label="* Comment", widget=forms.Textarea(attrs={'class': 'form-control'}), max_length=5000)
    captcha = ReCaptchaField()
