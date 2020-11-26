from django.db import models


class Post(models.Model):

    title = models.CharField(max_length=255)
    body = models.TextField(max_length=65000)
    date_added = models.DateTimeField('publication date')

    def __str__(self):
        return self.title


class Comment(models.Model):

    author_name = models.CharField(max_length=255)
    body = models.TextField(max_length=1000)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, default=None)
    date_added = models.DateTimeField('publication date')

    def __str__(self):
        return str(self.author_name) + ' - ' + self.date_added.strftime('%d.%m.%Y %H:%M')
