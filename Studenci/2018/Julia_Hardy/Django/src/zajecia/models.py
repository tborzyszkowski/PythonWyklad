from django.db import models
import random
import os
from django.urls import reverse
# Create your models here.


class Zajecia(models.Model):
    title = models.CharField(max_length=120)# chrfields are limited
    description = models.TextField()
    image = models.ImageField(upload_to='zajecia/', null=True, blank=True)

    def __str__(self):
        return self.title

