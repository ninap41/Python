# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect


# Create your views here.

def index(request):
    print "yo its working"
    return render(request, "valid_app/index.html")
