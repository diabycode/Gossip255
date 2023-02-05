from django.forms import ModelForm
from django import forms

from .models import CustomUser


class UserForm(ModelForm):

    class Meta:
        model = CustomUser
        fields = (
            "username",
            "password"
        )
        widgets = {
            "password": forms.PasswordInput()
        }



