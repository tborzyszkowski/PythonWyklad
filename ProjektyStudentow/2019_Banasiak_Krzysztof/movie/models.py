from django.db import models
from django.urls import reverse


class Type(models.Model):
    name = models.CharField(max_length=250)
    poster = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('movie:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.name


class Movie(models.Model):
    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    movie_title = models.CharField(max_length=250)
    director = models.CharField(max_length=250)
    is_watched = models.BooleanField(default=False)
    logo = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)

    def get_absolute_url(self):
        return reverse('movie:movies',)

    def __str__(self):
        return self.movie_title
