# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from .models import Course

# Create your views here.
def index(request):
    context = {
        'Courses': Course.objects.all()
    }
    print "yo its working"
    return render(request, "courses_app/index.html", context)

def destroy(request, Course_id):
    context = {
        'Course': Course.objects.get(id=Course_id)
    }
    print "You got em"
    return render(request, "courses_app/destroy.html", context)

def addcourse(request):
    name = request.POST['name']
    description = request.POST['description']
    Course.objects.create(name=name, description=description)
    print Course.objects.all().values()
    return redirect('/')

def deletecourse(request,Course_id):
    Course.objects.get(id=Course_id).delete()
    return render(request, "courses_app/destroy.html")

def goback(request):
    print "you will go back NOW"
    return redirect('/')