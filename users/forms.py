from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["email", "full_name", "username", "password"]

    password = forms.CharField(widget=forms.PasswordInput())
