from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

class Payment(models.Model):
    amount = models.FloatField(null=False)
    dueMonth = models.PositiveSmallIntegerField(null=False)
    service = models.ForeignKey("Service", related_name="payments")

    def __str__(self):
        return unicode(self.dueMonth).encode('utf-8')

    def isExpired(self):
        expired = False
        currentMonth = date.month()
        if self.dueMonth < currentMonth or (self.dueMonth == 12 and currentMonth == 1):
            expired = True
        return expired

class Service(models.Model):

    name = models.CharField(max_length=10)
    period = models.PositiveSmallIntegerField(null=False)
    phone = models.CharField(max_length=11, null=True)

    # Payments should be a list for save the last 12.
    # Add INFO: phone, owner, address, description

    def __str__(self):
        return unicode(self.name).encode('utf-8')

    def getPayment(self, month):
        try:
            payment = self.payments.get(dueMonth=month)
        except Payment.DoesNotExist:
            payment = None
        return payment

    def getPaymentsToShow(self):
        currentMonth = date.today().month
        possiblesMonths = (11,12,1,2,3,4,5,6,7,8,9,10,11,12,1,2)
        paymentsToShow = []
        if currentMonth-2 >= 1 and currentMonth+2 <= 12:
            for month in range(currentMonth-2,currentMonth+3):
                thisPayment = self.getPayment(month)
                amount = thisPayment and thisPayment.amount or 0
                paymentsToShow.append(amount)
        print paymentsToShow
        return paymentsToShow
