# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20150727_2012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='temporalavailability',
            options={'verbose_name_plural': 'Temporal Availabilities'},
        ),
    ]
