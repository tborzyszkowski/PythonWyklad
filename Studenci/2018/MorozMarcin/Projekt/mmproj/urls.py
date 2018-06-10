from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    url(r'^mmapp/', include('mmapp.urls')),
    url(r'^admin/', admin.site.urls),
]