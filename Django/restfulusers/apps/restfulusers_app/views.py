# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect,HttpResponse
from .models import User



# Create your views here.


def index(request):
    context = {
        'users': User.objects.all()
       
    }
    print "yo its working"
    return render(request, "restfulusers_app/index.html", context)

def newuser(request):
    print "create the user"
    return render(request, "restfulusers_app/create.html")

def createuser(request):
    firstname= request.POST['firstname']
    lastname= request.POST['lastname']
    email_address= request.POST['email']
    User.objects.create(firstname=firstname, lastname=lastname, email_address=email_address)
    print User.objects.all().values()
    return redirect('/')


def destroy(request,user_id):
    User.objects.get(id=user_id).delete()
    return redirect('/')

def edit(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    return render(request, "restfulusers_app/edit.html", context)

def update(request,user_id):
    edit = User.objects.get(id=user_id)
    edit.firstname= request.POST['firstname']
    edit.lastname= request.POST['lastname']
    edit.email_address= request.POST['email']
    edit.save()
    
    return redirect('/')

def show(request, user_id):
    context = {
        'user': User.objects.get(id=user_id)
    }
    print "create the user"
    return render(request, "restfulusers_app/show.html", context)

def goback(request):
    print "create the user"
    return redirect('/')






