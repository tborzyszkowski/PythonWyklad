Aplikacja do przchowywania muzyki w chmurze połączona z prostą funkcjonalnością wyświetlania memów.	
	
	
Bootstrap: 3.3.7 
Python: 3.6.1 
Django: 1.9.4 

*********************************************	
Najważniejsze Linki : 
*********************************************

 Krok po kroku pokazana i opisana każda istotna funkcjonalość. Jeżeli w poniżsym opisie nie ma wytłumaczonego zagadnienia którego poszukujesz, będzie ono wyłumaczoen w jednym z filmów.
 Video Tutorial:
https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK


Base Crud Tutorial
https://rayed.com/wordpress/?p=1266	
	
	
Informacji polecam też szukać w dokumetacji django.
https://docs.djangoproject.com/en/1.11/


*********************************************
Przydatne komendy(Cmd, Command Line,)
*********************************************
python manage.py createsuperuser
python manage.py runserver
python manage.py makemigrations
python manage.py migrate

python manage.py shell

from music.models import Nazwa_Modelu

Nazwa_Modelu.objects.filter(id=1)
Nazwa_Modelu.objects.all()
Nazwa_Modelu.XXX_set.count() # Nazwa_Modelu.song_set.count()
b = Album(artist ="Taylor", album_title="Red")
b.save()
	
	
*********************************************	
Search filter:
*********************************************
Chcąc dodać możliwość wyszukania objeków w bazie po specyficznym atrybucie, możemy zrobić to w sposób opisany oraz zaprezentowany ponieżej.

Akapit "Complex lookups with Q objects"
https://docs.djangoproject.com/en/1.11/topics/db/queries/
	
	
Przykład w kodzie:


### Przekazanie parametru/frazy po której chcielibyśmy przeszukać bazę do wiodoku wygląda w ten sposób.
### base.html =>
            <form class="navbar-form navbar-left" role="search" method="get" action="{% url 'music:index' %}">
                <div class="form-group">
                    <input type="text" class="form-control" name="q" value="{{ request.GET.q }}">
                </div>
                <button type="submit" class="btn btn-default">Search</button>
            </form>

### Zmienna query przyjmuje zawartość parametru "q", który otrzymujem z wywołania metody "Get" na widoku.
### query = request.GET.get("q")

### Nie będe tutaj opisywał dokładnej mechaniki działania "form" języka html. Konkretne infomacje oraz wytłumaczenie można znaleźć na stornie:
### https://www.w3schools.com/html/html_forms.asp

### Views.py => 

def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        albums = Album.objects.filter(user=request.user)
        song_results = Song.objects.all()
        query = request.GET.get("q")
        if query:
            albums = albums.filter(
                Q(album_title__icontains=query) |
                Q(artist__icontains=query)
            ).distinct()
            song_results = song_results.filter(
                Q(song_title__icontains=query)
            ).distinct()
            return render(request, 'music/index.html', {
                'albums': albums,
                'songs': song_results,
            })
        else:
            return render(request, 'music/index.html', {'albums': albums})