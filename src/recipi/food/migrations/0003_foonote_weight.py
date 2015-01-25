# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0002_auto_20150124_1717'),
    ]

    operations = [
        migrations.CreateModel(
            name='Foonote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, editable=False, unique=True)),
                ('number', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')], max_length=1)),
                ('nutrient_number', models.PositiveIntegerField(default=0)),
                ('text', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, editable=False, unique=True)),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('weight', models.DecimalField(max_digits=7, decimal_places=2)),
                ('data_points', models.PositiveIntegerField(default=0)),
                ('deviation', models.DecimalField(default=0.0, max_digits=7, decimal_places=3)),
                ('food', models.ForeignKey(to='food.FoodDescription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
