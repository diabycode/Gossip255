from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import AuthenticationForm

from .models import CustomUser


class UserAuthenticationForm(AuthenticationForm):

    username = forms.CharField(
        widget=forms.TextInput(
            attrs = {
                'placeholder': 'nom d\'utilisateur',
            }
        )
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs = {
                'placeholder': 'mot de passe'
            }
        )
    )
        

class UserSignUpForm(ModelForm):
    
    class Meta:
        model = CustomUser
        fields = "__all__"

        widgets = {
            "username": forms.TextInput(
                attrs={
                    "placeholder": "nom d'utilisateur"
                }
            ),
            "password": forms.PasswordInput(
                attrs={
                    "placeholder": "mot de passe",

                }
            )
        }


