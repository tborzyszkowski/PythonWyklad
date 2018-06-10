from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings

from . import views

app_name = 'mmapp'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^savedata/$', views.crud.savedata, name='savedata'),
    url(r'^updatedata/$', views.crud.updatedata, name='updatedata'),
    url(r'^([0-9]+)/editdata/$', views.crud.editdata, name='editdata'),
    url(r'^([0-9]+)/deletedata/$', views.crud.deletedata, name='deletedata'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
