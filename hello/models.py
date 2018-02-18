from django.db import models


# Create your models here.
class Greeting(models.Model):
    when = models.DateTimeField('date created', auto_now_add=True)
    on_delete = models.DO_NOTHING,


class Destinations(models.Model):
    title = models.CharField(max_length=500)
    price = models.FloatField()
    photoURL = models.CharField(max_length=600)
    description = models.CharField(max_length=2000)
    city_id = models.IntegerField()
    indoor_outdoor = models.CharField(max_length=100)
    day_night = models.CharField(max_length=100)

    def get_instance(self, instance_loader, row):
        # Returning False prevents us from looking in the
        # database for rows that already exist
        return False


class Time(models.Model):
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()
    city_id = models.IntegerField()


class Indoor(models.Model):
    isIndoor = models.BooleanField()
    city_id = models.IntegerField()
