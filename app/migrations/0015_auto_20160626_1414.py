# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-26 14:14
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_auto_20160626_1148'),
    ]

    operations = [
        migrations.AlterField(
            model_name='age',
            name='end_age',
            field=models.PositiveSmallIntegerField(verbose_name=b'Tot en met'),
        ),
        migrations.AlterField(
            model_name='age',
            name='from_age',
            field=models.PositiveSmallIntegerField(verbose_name=b'Van'),
        ),
    ]
