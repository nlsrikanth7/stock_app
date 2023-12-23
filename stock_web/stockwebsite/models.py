from django.db import models
from django_pandas.managers import DataFrameManager

# Create your models here.
class Tickersymbol(models.Model):
    ticker = models.CharField(max_length=20)
    tickerName = models.CharField(max_length=1000)

class Stockpricedata(models.Model):
    ticker = models.CharField(max_length=20, blank=True, null=True)
    Date = models.DateField(max_length=100, default='DEFAULT VALUE', blank=True, null=True)
    Open = models.FloatField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    High = models.FloatField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    Low = models.FloatField(max_length=140, blank=True, null=True)
    Close = models.FloatField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    AdjustedClose = models.FloatField(max_length=140, default='DEFAULT VALUE', blank=True, null=True)
    Volume = models.BigIntegerField(default='DEFAULT VALUE', blank=True, null=True)
    objects = models.Manager()
    # pdobjects = DataFrameManager()
    # objects = DataFrameManager()

    