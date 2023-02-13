from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import Comment


@admin.register(Comment)
class CommentAdmin(ModelAdmin):

    list_display = (
        "content",
        "post",
        "author",
        "created_at",
    )

