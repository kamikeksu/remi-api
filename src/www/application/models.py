from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from . import constants

class Category(models.Model):
    name = models.CharField(max_length=255, default='')

class User(models.Model):
    email = models.CharField(max_length=255, default='')
    password = models.TextField(default='')
    salt = models.TextField(default='')