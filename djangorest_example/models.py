from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)


class Employee(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(max_length=100, blank=True, null=True)
    company = models.ForeignKey(
        Company,
        related_name='employees',
        blank=True,
        null=True
    )
