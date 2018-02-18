from django.db import models

# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)


class Destinations(models.Model):
    title = models.CharField(max_length=50)
    price = models.FloatField()
    photoURL = models.CharField(max_length=300)
    description = models.CharField(max_length=1000)
    city_id = models.IntegerField()


class Time(models.Model):
    time = models.DateTimeField()
    city_id = models.IntegerField()


class Indoor(models.Model):
    isIndoor = models.BooleanField()
    city_id = models.IntegerField()
