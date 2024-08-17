from django.db import models

# Create your models here
class Post(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    
class Contact(models.Model):
    name = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    address = models.CharField(max_length=50)
    message = models.CharField(max_length=100)