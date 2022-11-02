from django.db import models
import datetime

class Message(models.Model):
    ish =models.CharField(max_length=200)
    rot = models.IntegerField()
    zac = models.CharField(max_length=200)
    date = models.CharField(max_length=200, default=str(datetime.datetime.now().year)+str(datetime.datetime.now().month)+str(datetime.datetime.now().day))


class UnMessage(models.Model):
    ish = models.CharField(max_length=200)
    rot = models.IntegerField()
    zac = models.CharField(max_length=200)