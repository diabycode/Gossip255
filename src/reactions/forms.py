from django.forms import ModelForm
from django import forms

from reactions.models import Comment


class PostCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ("content", )
        
        widgets = {
            "content": forms.Textarea(attrs={
                "placeholder": "publier un commentaire",
                "rows": "3",
            })
        }


