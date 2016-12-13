from django.db import models
from .query import CachingQuerySet


class CacheManager(models.Manager):
    """
    Custom model manager that returns CachingQuerySet
    """

    def get_queryset(self):
        return CachingQuerySet(self.model, using=self._db)

