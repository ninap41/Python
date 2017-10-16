from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^randomword$', views.randomword),
    url(r'^reset$', views.reset)

    # views.show is going to reference function on views
]
