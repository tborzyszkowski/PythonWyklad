from Question import views as v
from Question import forms as f
from django.conf.urls import include, url
from django.contrib.auth import views as auth

urlpatterns = [
    url(r'^(?P<page>[\d]*)/?$', v.Index.as_view(), name='index'),
    url(r'^(?P<page>[\d]+)/(?P<sortby>[\w\-]+)$', v.Index.as_view(), name='index'),
    url(r'^category/(?P<category>[\w\-\_]+)/(?P<page>[\d]+)/(?P<sortby>[\w\-]*)$', v.Index.as_view(), name='index'),
    url(r'^categories/(?P<page>[\d]*)', v.Categories.as_view(), name='categories'),
    url(r'^question/(?P<pk>[\d]+)', v.Question.as_view(), name='question'),
    url(r'^question/add', v.NewQuestion.as_view(), name='newQuestion'),
    url(r'^edit/answer/(?P<pk>[\d]+)', v.EditAnswer.as_view(), name='edit_answer'),
    url(r'^edit/question/(?P<pk>[\d]+)', v.EditQuestion.as_view(), name='edit_question'),
    url(r'^delete/answer/(?P<pk>[\d]+)', v.DeleteAnswer.as_view(), name='delete_answer'),
    url(r'^delete/question/(?P<pk>[\d]+)', v.DeleteQuestion.as_view(), name='delete_question'),
    url(r'^login/$', auth.login, {'template_name': 'auth/login.html', 'authentication_form': f.Login}),
    url(r'^logout/$', auth.logout, kwargs={'next_page': '/'}),
    url(r'^register/$', v.Register.as_view()),
]
