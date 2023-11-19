from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='products/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    def __str__(self):
        return self.title

class Transport(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Furniture(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Cloth(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title

class Sport(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='transport/%Y/%m/%d/')
    description = models.TextField()
    price = models.PositiveIntegerField()
    author = models.CharField(max_length=20, blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title
