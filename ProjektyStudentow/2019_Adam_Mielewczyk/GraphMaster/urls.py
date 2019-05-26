from django.urls import path

from . import views

app_name = 'graphmaster'
urlpatterns = [
    path('', views.index, name='index'),
    path('info', views.input, name='info'),
    path('izomorficznosc', views.input, name='izomorficznosc'),
    path('rysuj', views.input, name='rysuj'),
    path('dodaj', views.input, name='dodaj'),
    path('odejmij', views.input, name='odejmij'),
    path('neguj', views.input, name='neguj'),
    path('input', views.input, name='input'),
    path('<int:graph_id>/answer/', views.answer, name='answer'),
]
