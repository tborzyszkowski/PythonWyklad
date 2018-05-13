"""django_rental URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static


from instruktorzy.views import InstruktorListView, instruktor_list_view
from zajecia.views import ZajeciaListView, zajecia_list_view
from zapisy.views import zapisy_create, zapisy_list, zapisy_update, zapisy_delete, zapisy_detail

from .views import home_page, contact_page, login_page, logout_page, register_page, grafik, cennik
urlpatterns = [
    url(r'^$', home_page, name='home'),
    url(r'^contact/$', contact_page, name='contact'),
    url(r'^grafik/$', grafik, name='grafik'),
    url(r'^cennik/$', cennik, name='cennik'),
    url(r'^instruktorzy/$', InstruktorListView.as_view(), name='kadra'),
    url(r'^instruktorzy-fbv/$', instruktor_list_view),
    url(r'^zajecia/$', ZajeciaListView.as_view(), name='zajecia'),
    url(r'^zajecia-fbv/$', zajecia_list_view),
    url(r'^login/$', login_page, name='logowanie'),
    url(r'^logout/$', logout_page, name='logout'),
    url(r'^register/$', register_page, name='rejestracja'),
    url(r'^zapisy/$', zapisy_list, name="zapisy"),
    url(r'^zapisy/(?P<id>\d+)/$', zapisy_detail, name='detail'),
    url(r'^create/$', zapisy_create, name="create"),
    url(r'^zapisy/(?P<id>\d+)/edit/$', zapisy_update, name='update'),
    url(r'^zapisy/(?P<id>\d+)/delete/$', zapisy_delete),
    url(r'^admin/', admin.site.urls),
]


if settings.DEBUG:# w settings sekcja debug musi byc true"
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
