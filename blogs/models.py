from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(unique=True, null=False)
    bio = models.TextField(null=True)
    #avatar =

    #USERNAME_FIELD =
    REQUIRED_FIELDS = []

class Blog(models.Model):
    host = models.CharField(max_length=200, null=False)
    column = models.CharField( max_length=200, null=False)
    title = models.CharField(max_length=200, null=False)
    post = models.TextField(blank=False)
    #participants=
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.post

class Column(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.body
