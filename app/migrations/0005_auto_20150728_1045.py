# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20150727_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='annual_price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='month_price',
            field=models.DecimalField(null=True, max_digits=6, decimal_places=2, blank=True),
        ),
    ]
