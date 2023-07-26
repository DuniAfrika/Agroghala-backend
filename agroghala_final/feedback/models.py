from django.db import models
from users.models import NewUser


class FeedBack(models.Model):
    user = models.ManyToManyField(NewUser)
    email = models.EmailField()
    content = models.TextField()
