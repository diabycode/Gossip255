from django.db import models
from django.utils import timezone

from account.models import CustomUser


class HashTag(models.Model):
    name = models.CharField(max_length=50, blank=False)


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False)
    thumbnail = models.ImageField(blank=True, null=True)
    hashtags = models.ManyToManyField(HashTag, blank=True)
    published = models.BooleanField(default=False)
    create_on = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):

        # getting hashtags
        for word in self.content.split(" "):
            if word.startswith("#"):
                hashtag = HashTag.objects.create(name=word[1:])
                self.hashtags.set([hashtag])

        super().save(force_insert=False, force_update=False, using=None, update_fields=None)

