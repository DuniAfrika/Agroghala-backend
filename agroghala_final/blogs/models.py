from django.db import models
from django.utils import timezone
from users.models import NewUser
from django.conf import settings


class Blog(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, default="")
    content = models.TextField()
    views = models.IntegerField(default=0)
    image = models.ImageField(default='default.jpg', upload_to='blog_images/', blank=True)
    date_posted = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class Comment(models.Model):
    author = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    content = models.TextField()
    views = models.IntegerField(default=0)
    date_posted = models.DateTimeField(default=timezone.now)
    blog = models.ForeignKey('Blog', on_delete=models.CASCADE, null=True, related_name='comments')
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f"{self.athor.first_name}'s comment"
