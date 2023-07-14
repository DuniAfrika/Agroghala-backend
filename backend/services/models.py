from django.db import models

class Ghala(models.Model):
    title = models.CharField(max_length=50, blank=False)
    short_description = models.TextField()
    full_description = models.TextField()
    contact = models.CharField(max_length=10)
    location = models.CharField(max_length=50, null=True)
    email = models.EmailField()
    start_price = models.IntegerField(blank=False)
    rent_price = models.IntegerField(blank=False)
    on_demand = models.BooleanField(default=False)
    space_available = models.BooleanField(default=True)
    image = models.ImageField(default='default.jpg', upload_to='')

    def __str__(self):
        return self.title

class Soko(models.Model):
    commodity = models.CharField(unique=True, max_length=50)
    last_price = models.IntegerField()
    current_price = models.IntegerField()
    on_demand = models.BooleanField(default=False)
    image = models.ImageField(default='default.jpg', upload_to='')

    def __str__(self):
        return self.commodity
