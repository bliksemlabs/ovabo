# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 19:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0016_auto_20160627_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temporalavailability',
            name='notes',
            field=models.TextField(blank=True, verbose_name=b'Opmerkingen'),
        ),
    ]
