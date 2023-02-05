from django.contrib import admin

from .models import Post, HashTag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = ("content", "author")


@admin.register(HashTag)
class HashTagAdmin(admin.ModelAdmin):
    list_display = ("name", )

