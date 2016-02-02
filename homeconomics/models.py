from django.db import models
from dateutil.relativedelta import relativedelta
from datetime import date

class Service(models.Model):

    name = models.CharField(max_length=10)
    period = models.PositiveSmallIntegerField()
    toPay = models.FloatField()
    dueDate = models.DateField()
    # Payments should be a list for save the last 12.
    # Add INFO: phone, owner, address, description

    def __str__(self):
        return unicode(self.name).encode('utf-8')

    def expired(self):
	expired = False
	today = date.today()
	if self.dueDate < today:
	    expired = True
	return expired

    def setOnTable(self):
	"""
	IMPLEMENT DRAW LIST.
	method recieve a payment object and draw it
	"""
	self.payments = [(0,"") for m in range(5)]
	dif = self.dueDate.month - date.today().month
	if dif < 3:
	    self.payments[2 + dif] = (self.toPay, self.dueDate)
	elif dif > 9:
	    self.payments[2 + dif - 12] = (self.toPay, self.dueDate)

    def update(self):
        pass
    """
	lastSixMonths = sum(self.payments[n][0] for n in range(0,6))
	qtyMonthsNotZero = sum(self.payments[n][0] != 0 for n in range(0,6))
	if self.qtyMonthsPassed == self.period:
	    self.payments.append((lastSixMonths/qtyMonthsNotZero, self.dueDate + relativedelta(months=self.period)))
	    self.qtyMonthsPassed = 0
	else:
	    self.payments.append((0,""))
	del self.payments[0]
	self.dueDate += relativedelta(months=self.period)
	print self.qtyMonthsPassed
	# amounts
	amtPayments = [element[0] for element in self.payments]
	# save
        self.save()
    """

class Item(models.Model):

    name = models.CharField(max_length=20)
    stock = models.IntegerField()
    price = models.FloatField()
    
    def __str__(self):
        return unicode(self.name).encode('utf-8')
