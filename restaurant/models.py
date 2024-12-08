from django.db import models
from django.utils import timezone

# Create your models here.

class Booking(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,default='Default Name')
    no_of_guests = models.IntegerField(default=1)
    booking_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Menu(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255,default='Default Title')
    price = models.DecimalField(max_digits=10, decimal_places=2,default=0.00)
    inventory = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.title} : {self.price}'