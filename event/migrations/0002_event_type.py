# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 20:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='type',
            field=models.IntegerField(default=3),
            preserve_default=False,
        ),
    ]
