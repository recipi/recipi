# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDescription',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, unique=True, primary_key=True, blank=True, max_length=32, serialize=False)),
                ('ndb_no', models.CharField(max_length=5)),
                ('long_description', models.TextField()),
                ('short_description', models.TextField()),
                ('common_names', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('survey', models.BooleanField(default=False)),
                ('refuse_description', models.TextField(blank=True)),
                ('refuse', models.PositiveIntegerField(null=True, blank=True, default=None)),
                ('scientific_name', models.TextField(blank=True)),
                ('nitrogen_factor', models.DecimalField(decimal_places=2, max_digits=4, default=0.0)),
                ('protein_factor', models.DecimalField(decimal_places=2, max_digits=4, default=0.0)),
                ('fat_factor', models.DecimalField(decimal_places=2, max_digits=4, default=0.0)),
                ('carbohydrate_factor', models.DecimalField(decimal_places=2, max_digits=4, default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, unique=True, primary_key=True, blank=True, max_length=32, serialize=False)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Foonote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, unique=True, primary_key=True, blank=True, max_length=32, serialize=False)),
                ('number', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=1, choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')])),
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
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, unique=True, primary_key=True, blank=True, max_length=32, serialize=False)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('data_points', models.PositiveIntegerField(default=0)),
                ('deviation', models.DecimalField(decimal_places=3, max_digits=7, default=0.0)),
                ('food', models.ForeignKey(to='food.FoodDescription')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='fooddescription',
            name='food_group',
            field=models.ForeignKey(to='food.FoodGroup'),
            preserve_default=True,
        ),
    ]
