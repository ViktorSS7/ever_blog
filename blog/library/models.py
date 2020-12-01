from django.db import models


class BookCategory(models.Model):

    title = models.CharField(max_length=100)


class Book(models.Model):

    title = models.CharField(max_length=255)
    description = models.TextField(max_length=65000)
    category = models.ManyToManyField(BookCategory)
    link_on_image = models.TextField(max_length=1000)
    link_on_source = models.TextField(max_length=1000)


class BookFiles(models.Model):

    download_link = models.TextField(max_length=1000)
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    file_size = models.IntegerField()
    file_format = models.CharField(max_length=10)
