# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-10-01 20:44
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_auto_20170930_1338'),
    ]

    operations = [
        migrations.AddField(
            model_name='relationship',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='relationship',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
