from django.db import models
from django.utils import timezone

class Ghala(models.Model):
    title = models.CharField(max_length=50, default="")
    description = models.TextField()
    location = models.CharField(max_length=255)
    contact = models.CharField(max_length=10)
    email = models.EmailField()
    start_price = models.IntegerField()
    rent_price = models.IntegerField()
    on_demand = models.BooleanField(default=False)
    space_available = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg', upload_to='images')


    def __str__(self):
        return self.title

class Soko(models.Model):
    commodity = models.CharField(max_length=50, default="")
    last_price = models.IntegerField(default=0)
    current_price = models.IntegerField(default=0)
    on_demand = models.BooleanField()
    image = models.ImageField(default='default.jpg', upload_to='images')

    def __str__(self):
        return self.commodity


