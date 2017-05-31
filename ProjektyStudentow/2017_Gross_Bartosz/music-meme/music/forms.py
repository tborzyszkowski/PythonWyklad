from django import forms
from django.contrib.auth.models import User

from .models import Album, Song, Mem

class PageForm(forms.Form):
    page = forms.IntegerField()


class MemeForm(forms.ModelForm):

    class Meta:
        model = Mem
        fields = ['name', 'tag', 'image']

class AlbumForm(forms.ModelForm):

    class Meta:
        model = Album
        fields = ['artist', 'album_title', 'genre', 'album_logo']


class SongForm(forms.ModelForm):

    class Meta:
        model = Song
        fields = ['song_title', 'audio_file']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
