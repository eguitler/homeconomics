from django.contrib import admin
from models import Service, Item, History, Payment

admin.site.register(Service)
admin.site.register(History)
admin.site.register(Payment)
admin.site.register(Item)
