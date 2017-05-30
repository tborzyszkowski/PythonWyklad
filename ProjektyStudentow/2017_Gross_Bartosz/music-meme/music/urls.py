from django.conf.urls import url
from . import views

app_name = 'music'

urlpatterns = [
    #url(r'^edit/(?P<pk>\d+)$', views.ServerUpdate.as_view(), name='server_edit'),
    # url(r'^server_list/$', views.ServerList.as_view(), name='server_list'),
    url(r'^edit/(?P<pk>\d+)/$', views.mem_update, name='server_edit'),
    url(r'^mem_list/(?P<page>[0-9]+)/$', views.mem_list, name='mem_list'),

    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login_user/$', views.login_user, name='login_user'),
    url(r'^logout_user/$', views.logout_user, name='logout_user'),
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^mem/(?P<mem_id>[0-9]+)/$', views.detail_mem, name='detail_mem'),

    url(r'^(?P<song_id>[0-9]+)/favorite/$', views.favorite, name='favorite'),
    url(r'^songs/(?P<filter_by>[a-zA_Z]+)/$', views.songs, name='songs'),

    url(r'^create_album/$', views.create_album, name='create_album'),
    url(r'^create_mem/$', views.create_mem, name='create_mem'),

    url(r'^(?P<album_id>[0-9]+)/create_song/$', views.create_song, name='create_song'),
    url(r'^(?P<album_id>[0-9]+)/delete_song/(?P<song_id>[0-9]+)/$', views.delete_song, name='delete_song'),
    url(r'^(?P<album_id>[0-9]+)/favorite_album/$', views.favorite_album, name='favorite_album'),
    url(r'^(?P<album_id>[0-9]+)/delete_album/$', views.delete_album, name='delete_album'),
]
