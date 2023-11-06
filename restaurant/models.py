# from collections.abc import Any, Iterable
from django.db import models
import random 
import string
import datetime


# Create your models here.


class Reservations(models.Model):
    name = models.CharField(max_length=200)
    guest_number = models.IntegerField(default=0)
    date = models.DateField(default=datetime.datetime.now())
    time = models.TimeField()
    email = models.EmailField(max_length=200, default="example@anymail.com")
    ticket_number = models.CharField(unique=True, editable=False, max_length=9)

    #generating a random ticket number to be saved into the database
    # def save(self, *args, **kwargs):
    #     if not self.ticket_number:
    #         while True:
    #             ticket_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=8))
    #             if not Reservations.objects.filter(ticket_number=ticket_number).exists():
    #                 break
    #         self.ticket_number = ticket_number
    #     super(Reservations, self).save(*args, **kwargs)
    @property
    def expiration(self):
        date = datetime.datetime.combine(self.date, datetime.time.min)  # Combine date with midnight
        expiration_time = datetime.timedelta(minutes=1)
        current_time = datetime.datetime.now()
        print(date)
        print(expiration_time)
        print(current_time)
        if date <= current_time - expiration_time :
            return True
        else:
            return False
        
        

    def __str__(self):
        return self.name

class Menu(models.Model):
    menu = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=15, decimal_places=2, default=99.99)    

    def __str__(self):
        return self.menu
    
class Image(models.Model):
    image = models.ImageField(upload_to='images/')

class FoodCategories(models.Model):
    title = models.CharField(max_length=200)
    menu = models.ForeignKey(Menu, on_delete=models.SET_NULL, null=True)
    image = models.ForeignKey(Image, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return self.title