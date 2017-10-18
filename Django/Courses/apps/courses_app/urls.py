from django.conf.urls import url
from django.contrib import admin
from . import views
  
urlpatterns = [
        url(r'^$', views.index),
        url(r'^addcourse$', views.addcourse),
        url(r'^destroy/(?P<Course_id>\d+)$', views.destroy),
        url(r'^deletecourse/(?P<Course_id>\d+)$', views.deletecourse),
        url(r'^goback$', views.goback),

  ]
