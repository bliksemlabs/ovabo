# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_auto_20150728_1233'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='agegroup',
            name='product',
        ),
        migrations.AddField(
            model_name='product',
            name='agegroup',
            field=models.ForeignKey(default=0, to='app.AgeGroup'),
            preserve_default=False,
        ),
    ]
