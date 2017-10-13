# -*- coding: utf-8 -*-
from __future__ import unicode_literals 

from django.shortcuts import render, redirect

# Create your views here.

def index(request) :
 #this is like request.form
    print "Made It To Index"
    return render(request, "index.html")

def number(request,digit):
    context = { 'number':digit
    }
    print "Yo"
    return render(request, "number.html", context)

def destroy(request,digit):
    print "Hey"
    return redirect('/blogs/') 

def edit (request,digit):
    context = { 'number':digit
    }
    print "edit"
    return render(request, "edit.html", context)

