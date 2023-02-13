import django
from django.db import models
from django.shortcuts import get_object_or_404
from django.utils import timezone

from account.models import CustomUser
from reactions.models import Vote


class HashTag(models.Model):
    name = models.CharField(max_length=50, blank=False, unique=True)


class Post(models.Model):
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, blank=False)
    content = models.TextField(blank=False)
    thumbnail = models.ImageField(blank=True, null=True, upload_to="posts_thumb")
    hashtags = models.ManyToManyField(HashTag, blank=True)
    published = models.BooleanField(default=False)
    create_on = models.DateTimeField(default=timezone.now)
    edited = models.BooleanField(default=False)
    vote_count = models.IntegerField(default=0)

    def save(self, force_insert=False, force_update=False, using=None,
             update_fields=None):
        super().save(force_insert=force_insert, force_update=force_update, using=using, update_fields=update_fields)

        # getting hashtags
        hashtags = []
        for word in self.content.split(" "):
            if word.startswith("#"):
                hashtag = HashTag(name=word[1:])
                hashtags.append(hashtag)

        if hashtags:
            for hashtag in hashtags:
                try:
                    hashtag.save()
                except django.db.utils.IntegrityError:
                    pass

            self.hashtags.set([HashTag.objects.get(name=h.name) for h in hashtags])

    def update_vote(self, author):
        """
            Get or create a Vote model
            if create:
                - update vote count and save
                return 1
            else:
                - delete Vote object
                - update vote count and save
                - return -1
        """
        vote_object, created = Vote.objects.get_or_create(user=author, post=self)
        if created:
            self.vote_count += 1
            self.save()
            return 1

        vote_object.delete()
        self.vote_count -= 1
        self.save()
        return -1




