# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-16 22:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ninjas_app', '0002_auto_20171016_2155'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojos',
            name='desc',
            field=models.TextField(default='none'),
            preserve_default=False,
        ),
    ]
