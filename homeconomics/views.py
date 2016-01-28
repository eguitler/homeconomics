from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
import datetime, calendar
from forms import myForm
from models import Service

class Home(View):

    def get(self,request):
        form = myForm()
        services = Service.objects.all()
        context = {'services':services,
               'form':form
              }
        return render(request,'index.html',context)

    def post(self,request):
        form = myForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            option = form.cleaned_data['option']
        context = {'text':text,
               'option':option
              }
        return render(request,'response.html',context)

class Services(View):

    def get(self,request):
        services = Service.objects.all()
        today = datetime.datetime.now()
        for s in services:
            if s.nextPayDate.day == today.day and s.nextPayDate.month == today.month and s.nextPayDate.year == today.year:
                print "ACTUALIZAR FECHA"
            else:
                print "NO ACTUALIZA"
        context = { 'services':services,
                    'totalPaid': sum(s.lastAmountPaid for s in services),
                    'totalPay': sum(s.nextAmountToPay for s in services)
                  }
        return render(request,'services.html',context)

    def post(self,request):
        item = Service.objects.get(id=(request.POST['remove']))
        item.delete()
        services = Service.objects.all()
        context = { 'services':services,
                    'totalPaid': sum(s.lastAmountPaid for s in services),
                    'totalPay': sum(s.nextAmountToPay for s in services)
                  }
        return render(request,'services.html',context)

    def delete(self,request):
        pass

class Stock(View):

    def get(self,request):
        return render(request,'stock.html')

    def post(self,request):
        pass
