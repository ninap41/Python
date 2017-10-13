from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^(?P<digit>\d+)$', views.number),
    url(r'^(?P<digit>\d+)/edit$', views.edit), 
    url(r'^(?P<digit>\d+)/delete$', views.destroy), 
   
    # views.show is going to reference function on views
]
