# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 19:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20160627_1929'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='notes',
            field=models.TextField(blank=True, verbose_name=b'Opmerkingen'),
        ),
        migrations.AlterField(
            model_name='linegroup',
            name='notes',
            field=models.TextField(blank=True, verbose_name=b'Opmerkingen'),
        ),
    ]
