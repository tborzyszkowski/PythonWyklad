import datetime
from django.db import models
from django.utils import timezone

class Product(models.Model):
    name = models.CharField(max_length=200, blank='true')
    items = models.CharField(max_length=10)
    date = models.DateTimeField('date')
    image = models.FileField(upload_to='images', blank='true')
    shop = models.CharField(max_length=20)  #model.CharField(Shop)
    checked = models.CharField(max_length=1)
    class Meta:
        db_table = u'mmapp_product'

#    def __str__(self):
#        return self.items
    def get_absolute_url(self):
        return self.image

    def get_shop(self):
        shop_list = {
            "lidl": "Lidl",
            "biedr": "Biedronka",
            "auchan": "Auchan",
            "tesco": "Tesco",
            "inter": "Intermarche"
        }
        return shop_list[self.shop]

    def get_checked(self):
        return self.checked == '1' and "checked" or ""


class Shop(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20, blank='true')
    city = models.CharField(max_length=20, blank='true')
    addr = models.CharField(max_length=100, blank='true')
    lati = models.DecimalField(max_digits=10, decimal_places=1)
    long = models.DecimalField(max_digits=10, decimal_places=1)
    open = models.CharField(max_length=200, blank='true')