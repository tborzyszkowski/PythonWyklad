from django.contrib import admin
from django.urls import path
from graphene_django.views import GraphQLView
from django.http import HttpResponse

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', GraphQLView.as_view(graphiql=False)),
    path('graphiql/', GraphQLView.as_view(graphiql=True)),
    path('health/', lambda r: HttpResponse("OK")),
    path('', lambda r: HttpResponse("Hey kids, wanna see <a href='http://localhost:8000/graphiql/'>GraphQL</a>? :D"))
]
