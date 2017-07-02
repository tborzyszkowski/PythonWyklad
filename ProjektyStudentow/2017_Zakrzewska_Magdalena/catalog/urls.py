from django.conf.urls import url
from django.views.decorators.cache import cache_page
from . import views
from django.contrib.auth import views as auth_views

from . import views

app_name = 'catalog'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^add_article', views.AddArticleView, name='add_article'),
    url(r'^article/(?P<article_id>\d+)/$', views.ArticleDetailView.as_view(), name='article_detail'),
    url(r'^article/(?P<article_id>\d+)/comment/$', views.CommentView, name='comment'),
    url(r'^article/(?P<article_id>\d+)/like/$', views.LikeView, name='like'),
    url(r'^article/(?P<article_id>\d+)/dislike/$', views.DislikeView, name='dislike'),
    url(r'^accounts/register/$', views.RegisterAccountView, name='register'),
    url(r'^logout/$', views.LogOutView, name='logged_out'),
    url(r'^article/(?P<article_id>\d+)/comment_remove/(?P<comment_id>\d+)/$', views.CommentRemoveView, name='comment_remove')
]