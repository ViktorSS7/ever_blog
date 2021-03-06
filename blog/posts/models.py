import datetime

from django.db import models

from django.utils import timezone

from django.contrib.auth.models import User


class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField(max_length=65000)
    date_added = models.DateTimeField('publication date')

    def __str__(self):
        return self.title

    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.date_added <= now


class Comment(models.Model):

    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    body = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    date_added = models.DateTimeField('publication date')

    def __str__(self):
        return str(self.user.username) + ' - ' + self.date_added.strftime('%d.%m.%Y %H:%M')
