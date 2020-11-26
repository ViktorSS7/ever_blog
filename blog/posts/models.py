from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField(max_length=65000)
    date_added = models.DateTimeField('publication date')


class Comment(models.Model):

    author_name = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    date_added = models.DateTimeField('publication date')
