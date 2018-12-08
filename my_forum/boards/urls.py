from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index, name='index'),
    url(r'^boards/(?P<pk>\d+)/$', views.board_topics, name='board_topics'),
]

