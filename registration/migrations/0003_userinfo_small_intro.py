# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-29 19:11
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0002_userinfo_blog'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='small_intro',
            field=models.CharField(blank=True, max_length=300),
        ),
    ]
