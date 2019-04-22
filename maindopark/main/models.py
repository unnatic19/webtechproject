from django.conf import settings
from django.db import models


class login(models.Model):
    username = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    password = models.CharField(max_length=7, default='', editable=True)
    country_name = models.CharField(max_length=7, default='', editable=True)
    car_rides = models.IntegerField(default=0, editable=True)
    phone_number = models.IntegerField( default=0, editable=True)
    email = models.EmailField( default='', editable=True)