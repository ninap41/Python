# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse


# Create your views here.
def index(request):
    print "yo its working"
    return render(request, "multipleapps_app/index.html")