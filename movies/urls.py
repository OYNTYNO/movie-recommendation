from django.conf.urls import url
from . import views

app_name = 'movies'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<movie_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<movie_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<movie_id>[0-9]+)/results/$', views.results, name='results'),
]
