# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse

# from django.core.validators import validate_email
# from django.core.exceptions import ValidationError



def index(request):
    return HttpResponse("Go make some shell queries!")

# use this function to create users with validations

    
  
