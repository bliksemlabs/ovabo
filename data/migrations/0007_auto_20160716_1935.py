# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 19:35
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0006_auto_20160716_1924'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='publiclinenumber',
            field=models.CharField(max_length=25),
        ),
    ]
