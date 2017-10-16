# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect

# Create your views here.

def index(request):
    print "yo its working"
    return render(request, "surveyform_app/index.html")

def formprocess(request):
    if 'counter' in request.session:
        request.session['counter'] += 1
    else:
        request.session['counter'] = 1

    request.session['data'] = {
        "Name": request.POST['name'],
        "Dojo Location": request.POST['location'],
        "Favorite Language": request.POST['language'],
        "Comments": request.POST['comments']
    }
    return redirect('/showresults')

def showresults(request):
    print "Go to show results!"
    print request.session
    return render(request, 'surveyform_app/results.html')

