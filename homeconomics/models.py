from django.db import models
import datetime


class Service(models.Model):
    
    name = models.CharField(max_length=10)
    lastAmountPaid = models.FloatField()
    nextAmountToPay = models.FloatField()
    lastPayDate = models.DateField()
    nextPayDate  = models.DateField()

    def __str__(self):
        return unicode(self.name).encode('utf-8')

    def updateDates(self):
        self.lastPayDate = self.nextPayDate
        self.nextPayDate += datetime.timedelta(months=1)
        self.save()


class Item(models.Model):

    name = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return unicode(self.name).encode('utf-8')
