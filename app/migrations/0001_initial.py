# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('inclusive', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='LineGroup',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=32)),
                ('month_price', models.IntegerField()),
                ('annual_price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ProductReduction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=32)),
                ('reduction', models.IntegerField()),
                ('linegroup', models.ForeignKey(to='app.LineGroup')),
                ('product', models.ForeignKey(to='app.Product')),
            ],
        ),
        migrations.CreateModel(
            name='TemporalAvailability',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('description', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Weekdays',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('weekday', models.IntegerField(default=0)),
                ('from_time', models.TimeField()),
                ('to_time', models.TimeField()),
                ('productreduction', models.ForeignKey(to='app.TemporalAvailability')),
            ],
        ),
        migrations.AddField(
            model_name='productreduction',
            name='temporaryavailability',
            field=models.ForeignKey(to='app.TemporalAvailability'),
        ),
        migrations.AddField(
            model_name='line',
            name='linegroup',
            field=models.ForeignKey(to='app.LineGroup'),
        ),
    ]
