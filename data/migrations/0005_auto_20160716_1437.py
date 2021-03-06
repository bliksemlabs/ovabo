# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0004_auto_20160716_1422'),
    ]

    operations = [
        migrations.AlterField(
            model_name='line',
            name='average_km_rate',
            field=models.DecimalField(blank=True, decimal_places=5, max_digits=8, null=True, verbose_name='Gemiddeld tarief'),
        ),
        migrations.AlterField(
            model_name='line',
            name='maximum',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True, verbose_name='Maximum eenheden'),
        ),
    ]
