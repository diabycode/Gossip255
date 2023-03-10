from django.forms import ModelForm
from django import forms

from .models import Post


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = (
            "content",
            "thumbnail",
            "published",
        )
        widgets = {
            "content": forms.Textarea(attrs={
                "placeholder": "De quoi voulez-vous parler ?",
                "rows": "5",
            })
        }

