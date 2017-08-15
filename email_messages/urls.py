from django.conf.urls import url

from . import views
app_name = 'email_messages'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]
