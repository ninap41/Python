from django.conf.urls import url
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', views.index),
    url(r'^process$', views.formprocess),  #RED URL ####VIEW.FUNCTION
    url(r'^showresults$', views.showresults),

]
