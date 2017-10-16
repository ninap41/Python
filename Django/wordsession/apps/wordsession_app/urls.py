from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^getWord$', views.getWord),
    url(r'^clear$', views.clear),
  
    
   
    # views.show is going to reference function on views
]
