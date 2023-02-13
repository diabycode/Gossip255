from django.db import models

from django import apps
from gossip225 import settings


class Comment(models.Model):
    content = models.TextField()
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now=True)


class Vote(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post = models.ForeignKey("post.Post", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)



