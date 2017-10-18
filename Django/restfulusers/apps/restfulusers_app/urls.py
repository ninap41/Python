from django.conf.urls import url
from django.contrib import admin
from . import views
  
urlpatterns = [
        url(r'^$', views.index),
        url(r'^newuser$', views.newuser),
        url(r'^createuser$', views.createuser),
        url(r'^delete/(?P<user_id>\d+)$', views.destroy),
        url(r'^update/(?P<user_id>\d+)$', views.update),
        url(r'^edit/(?P<user_id>\d+)$', views.edit),
        url(r'^show/(?P<user_id>\d+)$', views.show),
        url(r'^goback$', views.goback),
]