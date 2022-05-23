from tkinter import CASCADE
from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(unique=True, null=True)
    bio = models.TextField(null=True)
    #avatar =

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

class Column(models.Model):
    name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    host = models.ForeignKey(User, on_delete=models.CASCADE)
    column = models.ForeignKey(Column, on_delete=models.CASCADE)
    title = models.CharField(max_length=200, null=True)
    post = models.TextField(blank=False)
    #participants=
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):        
        return self.title

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateField(auto_now=True)
    updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.body
