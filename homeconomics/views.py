from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
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
