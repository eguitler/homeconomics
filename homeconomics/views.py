from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from datetime import date
import calendar
from dateutil.relativedelta import relativedelta
from forms import myForm
from models import Service

class Home(View):

    def get(self,request):
        form = myForm()
        services = Service.objects.all()
        context = { 'services':services,
                    'form':form
                  }
        return render(request,'index.html',context)

    def post(self,request):
        form = myForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            option = form.cleaned_data['option']
        context = { 'text':text,
                    'option':option
                  }
        return render(request,'response.html',context)

class Services(View):

    def get(self,request):
        services = Service.objects.all()
        toShow = []
        for s in services:
            aService = (s.name, s.getPaymentsToShow())
            toShow.append(aService)
        totals = self.getTotal(toShow)
        context = { 'months': self.setMonths(date.today().month),
                    'services': toShow,
                    'totals': totals,
                  }
        return render(request,'services.html',context)

    def post(self,request):
        item = Service.objects.get(id=(request.POST['remove']))
        item.delete()
        services = Service.objects.all()
	totals = [[s.payments[n][0] for s in services] for n in range(0,5)]
        totals = [sum(month) for month in totals]
        context = { 'months': self.setMonths(today.month),
                    'services': services,
                    'totals': totals,
                  }
        return render(request,'services.html',context)

    def delete(self,request):
        pass

    def getTotal(self, months):
        pass

    def setMonths(self,currentMonth):
        months = ['October','November','December','January','February','March',
                  'April','May','June','July','August','September','October',
                  'November','December','January','February']
	return months[currentMonth:currentMonth+5:]

class Stock(View):

    def get(self,request):
        return render(request,'stock.html')

    def post(self,request):
        pass
