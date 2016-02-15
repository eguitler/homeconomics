from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

class Payment(models.Model):
    period = models.PositiveSmallIntegerField(null=False)
    amount = models.FloatField(null=False)
    dueDate = models.DateField(null=False)
    service = models.ForeignKey("Service", related_name="payments")

    def isExpired(self):
        expired = False
        today = date.today()
        if self.dueDate < today:
            expired = True
        return expired

    def update(self):
        pass

class Service(models.Model):

    name = models.CharField(max_length=10)
    # Payments should be a list for save the last 12.
    # Add INFO: phone, owner, address, description

    def __str__(self):
        return unicode(self.name).encode('utf-8')

    def getPayment(self, month):
        print payments.objects.all()
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

    def setOnTable(self):
	"""
	IMPLEMENT DRAW LIST.
	method recieve a payment object and draw it
	"""
        tmp = [payments.getPayment(m) for m in range(5)]
        self.payments = [(m.amount,"") for m in tmp]
