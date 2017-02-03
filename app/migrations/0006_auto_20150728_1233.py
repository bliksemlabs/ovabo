# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_auto_20150728_1045'),
    ]

    operations = [
        migrations.CreateModel(
            name='Age',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('from_age', models.IntegerField()),
                ('end_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='AgeGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=32)),
                ('product', models.ForeignKey(to='app.Product')),
            ],
        ),
        migrations.AddField(
            model_name='age',
            name='agegroup',
            field=models.ForeignKey(to='app.AgeGroup'),
        ),
    ]
