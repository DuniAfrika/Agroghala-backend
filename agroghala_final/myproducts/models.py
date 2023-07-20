from django.db import models
from users.models import NewUser
from services.models import *

class MyGhala(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    ghala = models.ManyToManyField(Ghala)
    bags_sold = models.IntegerField(default=0)
    date_rented = models.DateTimeField()
    duration_of_storage = models.IntegerField(default=3)

    def __str__(self):
        return f"{self.user} rented {self.ghala}"

class MySoko(models.Model):
    user = models.ForeignKey(NewUser, on_delete=models.CASCADE)
    commodity = models.ManyToManyField(Soko)
    bags_sold = models.IntegerField(default=0)
    date_sold = models.DateTimeField()

    def __str__(self):
        return f"{self.user} sold {self.commodity}"
