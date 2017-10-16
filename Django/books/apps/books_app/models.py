# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.



class books(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField()
    created_at= models.DateField(auto_now= True)
    updated_at= models.DateField(auto_now= True)
    

class authors(models.Model):
    first_name=models.CharField(max_length=255)
    last_name=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    books = models.ManyToManyField(books, related_name="authors")
    created_at= models.DateField(auto_now= True)
    updated_at= models.DateField(auto_now= True)

