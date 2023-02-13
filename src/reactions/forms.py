from django.forms import ModelForm

from reactions.models import Comment


class PostCommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ("content", )


