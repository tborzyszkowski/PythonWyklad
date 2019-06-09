from django.urls import path
from . import views

app_name = 'movie'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),

    path('movies/', views.Index2View.as_view(), name='movies'),

    path('<int:pk>/', views.DetailView.as_view(), name='detail'),

    path('add/', views.TypeCreate.as_view(), name='type-add'),

    path('<int:pk>/update', views.TypeUpdate.as_view(), name='type-update'),

    path('type/<int:pk>/delete', views.TypeDelete.as_view(), name='type-delete'),

    path('add-movie', views.MovieCreate.as_view(), name='movie-add'),

    path('movies/<int:pk>/update', views.MovieUpdate.as_view(), name='movie-update'),

    path('movies/<int:pk>/delete', views.MovieDelete.as_view(), name='movie-delete'),
]
