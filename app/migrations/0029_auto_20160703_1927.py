# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 19:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0028_remove_product_age_group'),
    ]

    operations = [
        migrations.RenameField(
            model_name='line',
            old_name='inclusive',
            new_name='pattern'
        ),
    ]