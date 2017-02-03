# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20150728_1237'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agegroup',
            name='description',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='line',
            name='inclusive',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='linegroup',
            name='description',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='productreduction',
            name='description',
            field=models.CharField(max_length=64),
        ),
        migrations.AlterField(
            model_name='temporalavailability',
            name='description',
            field=models.CharField(max_length=64),
        ),
    ]
