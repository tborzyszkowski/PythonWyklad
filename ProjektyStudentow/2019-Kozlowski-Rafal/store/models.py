from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.db import connection

class stocks(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('magazine-detail', kwargs={'pk': self.pk})


class clients(models.Model):
    First_name = models.CharField(max_length=15)
    Last_name = models.CharField(max_length=25)

    def __str__(self):
        return self.First_name + ' ' + self.Last_name

    def get_absolute_url(self):
        return reverse('clients')


class sells(models.Model):
    transaction_date = models.DateTimeField(default=timezone.now)
    client = models.ForeignKey(clients, on_delete=models.CASCADE)
    stock = models.ForeignKey(stocks, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse('sales-detail', kwargs={'pk': self.pk})