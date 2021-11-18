from django.db import models
from django.contrib.postgres.fields import ArrayField


# Create your models here.

class Book(models.Model):
    name = models.CharField(max_length=255)
    isbn = models.CharField(max_length=20, blank=True, null=True)
    authors = ArrayField(models.CharField(max_length=255))
    number_of_pages = models.IntegerField(blank=True, null=True)
    publisher = models.CharField(max_length=255, blank=True, null=True)
    country = models.CharField(max_length=255, blank=True, null=True)
    release_date = models.DateField(blank=True, null=True)
