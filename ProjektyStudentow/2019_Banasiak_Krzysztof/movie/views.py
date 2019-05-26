from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from.models import Type, Movie


## w index
class IndexView(generic.ListView):
    template_name = 'movie/index.html'
    context_object_name = 'all_types'

    def get_queryset(self):
        return Type.objects.all()


class Index2View(generic.ListView):
    template_name = 'movie/index2.html'
    context_object_name = 'all_movies'

    def get_queryset(self):
        return Movie.objects.all()


## w detail
class DetailView(generic.DetailView):
    model = Type
    template_name = 'movie/detail.html'


class TypeCreate(CreateView):
    model = Type
    fields = ['name', 'poster']


class TypeUpdate(UpdateView):
    model = Type
    fields = ['name', 'poster']


class TypeDelete(DeleteView):
    model = Type
    success_url = reverse_lazy('movie:index')


class MovieCreate(CreateView):
    model = Movie
    fields = ['type', 'movie_title', 'director',
              'is_watched', 'logo', 'description']


class MovieUpdate(UpdateView):
    model = Movie
    fields = ['type', 'movie_title', 'director',
              'is_watched', 'logo', 'description']


class MovieDelete(DeleteView):
    model = Movie
    success_url = reverse_lazy('movie:movies')


