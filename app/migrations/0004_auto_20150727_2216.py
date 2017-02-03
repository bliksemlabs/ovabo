# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20150727_2047'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='annual_price',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='month_price',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
