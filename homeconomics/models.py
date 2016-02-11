from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

class Payment(models.Model):
    period = models.PositiveSmallIntegerField()
    amount = models.FloatField()
    dueDate = models.DateField()
    
    def isExpired(self):
	expired = False
	today = date.today()
	if self.dueDate < today:
	    expired = True
	return expired

    def update(self):
        pass
    
class History(models.Model):
    
    payments = models.ForeignKey(Payment)

    def getPayment(self,month):
        print Payment.objects.all()
        try:
            payment = Payment.objects.get(dueDate__month='month')
        except ValueError:
            print "error"
            payment.amount = 0
        return payment 

    def checkPayments(self):
        for p in Payment.objects.all():
            if p.isExpired():
                p.update()

class Service(models.Model):

    name = models.CharField(max_length=10)
    history = models.ForeignKey(History)
    # Payments should be a list for save the last 12.
    # Add INFO: phone, owner, address, description

    def __str__(self):
        return unicode(self.name).encode('utf-8')
    
    def getPayment(self,month):
        return Payment.objects.all()

    def checkPayments(self):
        self.history.checkPayments()

    def setOnTable(self):
	"""
	IMPLEMENT DRAW LIST.
	method recieve a payment object and draw it
	"""
	tmp = [self.history.getPayment(m) for m in range(5)]
        self.payments = [(m.amount,"") for m in tmp]



class Item(models.Model):

    name = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return unicode(self.name).encode('utf-8')
