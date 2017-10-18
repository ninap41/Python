# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

class User(models.Model):
    firstname = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    email_address = models.CharField(max_length=255)
    created_at = models.DateField(auto_now= True)
    updated_at = models.DateField(auto_now = True)
