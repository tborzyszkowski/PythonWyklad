from django.contrib.auth.models import Permission, User
from django.db import models

from django.db import models
from django.core.urlresolvers import reverse

class Album(models.Model):
    user = models.ForeignKey(User, default=1)
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.FileField()
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    song_title = models.CharField(max_length=250)
    audio_file = models.FileField(default='')
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        return self.song_title

class Mem(models.Model):
    user = models.ForeignKey(User, default=1)
    name =  models.CharField(max_length=250)
    tag = models.CharField(max_length=160)
    image = models.FileField()
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('server_edit', kwargs={'pk': self.pk})