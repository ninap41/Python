# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

def index(request) :
 #this is like request.form
    print "Made It To Index"
    return render(request, "index.html")

def results(request) :
 #this is like request.form
    print "Made It To Index"
    return render(request, "results.html")
