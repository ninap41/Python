# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect, HttpResponse

# Create your views here.

def index(request):
    print "yo its working"
    return render(request, "surveyform_app/index.html")

def create(request):
	if request.method == "POST":
		print "*"*50
		print request.POST
        print request.POST['name']
        print request.POST['desc']
        request.session['name'] = "test"  # more on session below
	return redirect("/results")
   



# def process(request):
#     print "yo its working"
#     return render(redirect, "results.html")
