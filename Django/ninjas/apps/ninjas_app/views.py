from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print "yo its working"
    return render(request, "ninjas_app/index.html")