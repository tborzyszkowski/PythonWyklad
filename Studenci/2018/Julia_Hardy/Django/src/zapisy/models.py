from django.db import models
from django.conf import settings
from django.core.urlresolvers import reverse
from django.contrib.auth import get_user_model
from zajecia.models import Zajecia

# Create your models here.
User = settings.AUTH_USER_MODEL

class Zapisy(models.Model):
    CHOICELIST = (
        ('1', 'Modern jazz'),
        ('2', 'Modern balet'),
        ('3', 'Afro dance'),
        ('4', 'Break dance'),
    )
    HOUR = (
        ('1', '10:00'),
        ('2', '16:00'),
        ('3', '18:00'),
        ('4', '20:00'),
    )
    DAY = (
        ('1', 'Poniedziałek'),
        ('2', 'Wtorek'),
        ('3', 'Środa'),
        ('4', 'Czwartek'),
        ('4', 'Piątek'),
        ('4', 'Sobota'),
    )
    your_choice = models.CharField(max_length=1, choices=CHOICELIST, null=True)
    day_choice = models.CharField(max_length=1, choices=DAY, null=True)
    hour_choice = models.CharField(max_length=1, choices=HOUR, null=True)
    user = models.ForeignKey(get_user_model(), default=1)

#on_delete=models.CASCADE

    def __str__(self):
        return self.your_choice

    def get_absolute_url(self):
        return reverse("detail", kwargs={"id": self.id})
