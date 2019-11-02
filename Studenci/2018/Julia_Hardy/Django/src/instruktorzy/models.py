from django.db import models
from django.urls import reverse

# Create your models here.
# jak tworzymy modele to zawsze potem python manage.py makemigrations , migrate


class Instruktor(models.Model):
    title = models.CharField(max_length=120)# chrfields are limited
    description = models.TextField()
    image = models.ImageField(upload_to='instruktorzy/', null=True, blank=True)

    def __str__(self):
        return self.title

