from django.db import models
from django import forms



class Form(models.Model):
    visitor_name = models.CharField(max_length=20)
    email = models.EmailField(blank=True, verbose_name="Email(optional):")
    subject = models.CharField(max_length=20)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'Message from {self.visitor_name}'


class Cache(models.Model):
    """
    Model to represent cache entries in the django_cache table.
    This will allow us to visualize the cache contents.
    """
    key = models.CharField(max_length=255, unique=True)  # Cache key
    value = models.TextField()  # Cache value (stored as a string, which is how it's serialized in the cache)
    expire_time = models.DateTimeField()  # When the cache entry will expire

    def __str__(self):
        return f"{self.key} (expires at {self.expire_time})"