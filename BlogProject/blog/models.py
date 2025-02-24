from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
class Tag(models.Model):
    tag = models.CharField(max_length=100)
class Post(models.Model):
    title = models.CharField(max_length=70)
    body = models.TextField()
    