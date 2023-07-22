from django.db import models

class FeedBack(models.Model):
    email = models.EmailField()
    content = models.TextField()
