# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-16 18:02
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import utils.enums


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0036_auto_20160716_1456'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location_type', django_enumfield.db.fields.EnumField(default=1, enum=utils.enums.LocationType, verbose_name=b'Type')),
                ('online_url', models.CharField(blank=True, help_text=b'Indien online, URL waar dit product te koop is', max_length=256, null=True, verbose_name=b'Link')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='locations', to='app.Product')),
            ],
        ),
    ]