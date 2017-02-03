# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-03 13:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django_enumfield.db.fields
import utils.enums


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20160627_2019'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductBearer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bearer', django_enumfield.db.fields.EnumField(default=0, enum=utils.enums.Bearers)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='product_director',
            field=models.CharField(choices=[(b'ARR', b'Arriva'), (b'VTN', b'Veolia'), (b'CXX', b'Connexxion'), (b'EBS', b'EBS'), (b'GVB', b'GVB'), (b'HTM', b'HTM'), (b'NS', b'Nederlandse Spoorwegen'), (b'RET', b'RET'), (b'SYNTUS', b'Syntus'), (b'QBUZZ', b'Qbuzz'), (b'TCR', b'Taxi Centrale Renesse'), (b'GOVI', b'GOVI'), (b'VEO', b'Veolia (Trein)'), (b'NOORD', b'Arriva (Trein)'), (b'SYN', b'Syntus (Trein)'), (b'BRENG', b'Breng (CXX, Trein)'), (b'VALLEI', b'Valleilijn (CXX, Trein)'), (b'DB', b'DB (NS, Trein)'), (b'NSI', b'NS International (NS, Trein)'), (b'NMBS', b'NMBS (NS, Trein)'), (b'KEO', b'Keolis (Trein)')], default='NS', max_length=6, verbose_name=b'Productregisseur'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='product',
            name='product_owner',
            field=models.CharField(choices=[(b'ARR', b'Arriva'), (b'VTN', b'Veolia'), (b'CXX', b'Connexxion'), (b'EBS', b'EBS'), (b'GVB', b'GVB'), (b'HTM', b'HTM'), (b'NS', b'Nederlandse Spoorwegen'), (b'RET', b'RET'), (b'SYNTUS', b'Syntus'), (b'QBUZZ', b'Qbuzz'), (b'TCR', b'Taxi Centrale Renesse'), (b'GOVI', b'GOVI'), (b'VEO', b'Veolia (Trein)'), (b'NOORD', b'Arriva (Trein)'), (b'SYN', b'Syntus (Trein)'), (b'BRENG', b'Breng (CXX, Trein)'), (b'VALLEI', b'Valleilijn (CXX, Trein)'), (b'DB', b'DB (NS, Trein)'), (b'NSI', b'NS International (NS, Trein)'), (b'NMBS', b'NMBS (NS, Trein)'), (b'KEO', b'Keolis (Trein)')], default='NS', max_length=6, verbose_name=b'Producteigenaar'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='weekdays',
            name='from_time',
            field=models.TimeField(verbose_name=b'Van'),
        ),
        migrations.AlterField(
            model_name='weekdays',
            name='to_time',
            field=models.TimeField(verbose_name=b'Tot'),
        ),
        migrations.AlterField(
            model_name='weekdays',
            name='weekday',
            field=django_enumfield.db.fields.EnumField(default=0, enum=utils.enums.Weekday, verbose_name=b'Geldigheid'),
        ),
        migrations.AddField(
            model_name='productbearer',
            name='products',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Product', verbose_name=b'bearers'),
        ),
    ]
