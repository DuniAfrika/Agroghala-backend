from django.db import models
from services.models import *
from django.utils import timezone

class Myghala(models.Model):
    @property
    def amount_paid_new(self):
        start_price = self.ghala.start_price
        rent_price = self.ghala.rent_price
        return start_price + (rent_price * self.bags_stored * self.duration_of_storage)

    @property
    def amount_paid(self):
        rent_price = self.ghala.rent_price
        return (rent_price * self.bags_stored * self.duration_of_storage)

    ghala = models.ForeignKey(Ghala, on_delete=models.CASCADE)
    bags_stored = models.IntegerField()
    duration_of_storage = models.IntegerField(null=True)
    #amount_paid = amount_paid()
    rented_on = models.DateTimeField()

    def __str__(self):
        return str(self.ghala)


class Mysoko(models.Model):
    soko = models.ForeignKey(Soko, on_delete=models.CASCADE)
    bags_sold = models.IntegerField(null=True)
    sold_on = models.DateTimeField()

    @property
    def amount_accredited(self):
        price_of_commodity = self.soko.current_price

        return price_of_commodity * self.bags_sold


    def __str__(self):
        return str(self.soko)
