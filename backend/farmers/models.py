from django.db import models
from django.contrib.auth.models import AbstractUser

class Farmer(models.Model):
    first_name = models.CharField(max_length=50, default="")
    last_name = models.CharField(max_length=50, default="")
    email = models.EmailField(unique=True)
    phone = models.IntegerField(default=None, unique=True)
    location = models.CharField(max_length=50)

    def __str__(self):
        return self.first_name

