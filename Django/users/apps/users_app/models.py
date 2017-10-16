# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Users(models.Model):
    first_name= models.CharField(max_length=255)
    last_name= models.CharField(max_length=255)
    email_address= models.CharField(max_length=255)
    age = models.IntegerField()
    created_at= models.DateField(auto_now= True)
    updated_at= models.DateField(auto_now = True)
    


# Create your models here.
