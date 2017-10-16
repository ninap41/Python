# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime
from datetime import datetime


# Create your views here.

def index(request):
    print "It works"
   
    return render(request, "wordsession_app/index.html")

def getWord(request):
    

    newword = {}
    for key, value in request.POST.iteritems():
        if key != "csrfmiddlewaretoken" and key != "showbig":
            newword[key] = value
        if key == "showbig":
            newword['big'] = "big"
    
    newword['created_at'] = datetime.now().strftime("%H:%M %p, %B %d, %Y")
    
    try:
        request.session['words']
    except KeyError:
        request.session['words'] = []
    
    log = request.session['words']
    log.append(newword)
    request.session['words'] = log
    for key, val in request.session.__dict__.iteritems():
        print key, val


    return render(request, "wordsession_app/index.html", newword)

def clear(request):
     for key in request.session.keys():
        del log 
        return redirect('/')
