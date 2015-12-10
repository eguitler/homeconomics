from django.db import models

class Service(models.Model):
    
    name = models.CharField(max_length=10)
    lastAmountPaid = models.FloatField()
    nextAmountToPay = models.FloatField()
    lastPayDate = models.DateField()
    nextPayDate  = models.DateField()

    def __str__(self):
        return unicode(self.name).encode('utf-8')

class Item(models.Model):

    name = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return unicode(self.name).encode('utf-8')
