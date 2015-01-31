# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0013_auto_20150131_1939'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, editable=False, unique=True, blank=True, primary_key=True, max_length=32)),
                ('nutrient_id', models.CharField(max_length=3)),
                ('nutrient_value', models.DecimalField(max_digits=10, decimal_places=3)),
                ('min', models.DecimalField(max_digits=10, decimal_places=3)),
                ('max', models.DecimalField(max_digits=10, decimal_places=3)),
                ('degrees_of_freedon', models.PositiveIntegerField()),
                ('lower_error_bound', models.DecimalField(max_digits=10, decimal_places=3)),
                ('upper_error_bound', models.DecimalField(max_digits=10, decimal_places=3)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientDefinition',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, editable=False, unique=True, blank=True, primary_key=True, max_length=32)),
                ('nutrient_id', models.CharField(unique=True, max_length=3)),
                ('units', models.CharField(max_length=7)),
                ('tagname', models.CharField(blank=True, max_length=20)),
                ('description', models.CharField(blank=True, max_length=60)),
                ('decimal_places', models.PositiveIntegerField()),
                ('ordering', models.PositiveIntegerField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='nutrient',
            unique_together=set([('food', 'nutrient_id')]),
        ),
        migrations.RemoveField(
            model_name='weight',
            name='data_points',
        ),
    ]
