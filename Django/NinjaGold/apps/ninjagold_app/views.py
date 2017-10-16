from __future__ import unicode_literals
from django.shortcuts import render, HttpResponse, redirect


def index(request):
    print "yo its working"
    return render(request, "ninjagold_app/index.html")