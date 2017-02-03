# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_auto_20150728_1310'),
    ]

    operations = [
        migrations.AddField(
            model_name='line',
            name='transportmode',
            field=models.IntegerField(default=0),
        ),
    ]
