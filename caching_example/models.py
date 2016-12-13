from django.db import models
from .manager import CacheManager


class Author(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

    objects = CacheManager()


class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, related_name='books')
