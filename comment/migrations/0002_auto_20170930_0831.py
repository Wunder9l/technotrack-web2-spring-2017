# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-09-30 08:31
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='edited_count',
            field=models.IntegerField(default=0),
        ),
    ]
