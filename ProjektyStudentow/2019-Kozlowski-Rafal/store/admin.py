from django.contrib import admin
from .models import stocks, clients, sells

admin.site.register(stocks)
admin.site.register(clients)
admin.site.register(sells)