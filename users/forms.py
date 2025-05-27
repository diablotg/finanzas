from django import forms
from .models import User


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_confirm = forms.CharField(
        widget=forms.PasswordInput, label="confirm password"
    )

    class Meta:
        model = User
        fields = ["email", "full_name"]

    def clean_password_confirm(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password_confirm"]:
            raise forms.ValidationError("passwords do not match")
        return cd["password_confirm"]
