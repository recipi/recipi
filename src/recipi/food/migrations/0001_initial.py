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
            name='Food',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('ndb_number', models.CharField(max_length=5)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
                ('scientific_name', models.TextField(blank=True)),
                ('common_names', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('manufacturer_name', models.TextField(blank=True)),
                ('survey', models.NullBooleanField(default=None)),
                ('refuse_description', models.TextField(blank=True)),
                ('refuse_percentage', models.PositiveIntegerField(null=True, default=None, blank=True)),
                ('nitrogen_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('protein_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('fat_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
                ('carbohydrate_factor', models.DecimalField(decimal_places=2, default=0.0, max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('sequence', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')], max_length=1)),
                ('nutrient_id', models.CharField(max_length=3)),
                ('text', models.TextField()),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('factor_code', models.CharField(max_length=5)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LanguageDescription',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('factor_code', models.CharField(unique=True, max_length=5)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('nutrient_id', models.CharField(max_length=3)),
                ('nutrient_value', models.DecimalField(decimal_places=3, max_digits=10)),
                ('min', models.DecimalField(decimal_places=3, max_digits=10)),
                ('max', models.DecimalField(decimal_places=3, max_digits=10)),
                ('degrees_of_freedon', models.PositiveIntegerField()),
                ('lower_error_bound', models.DecimalField(decimal_places=3, max_digits=10)),
                ('upper_error_bound', models.DecimalField(decimal_places=3, max_digits=10)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='NutrientDefinition',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('units', models.CharField(max_length=7)),
                ('tagname', models.CharField(max_length=20, blank=True)),
                ('description', models.CharField(max_length=60, blank=True)),
                ('decimal_places', models.PositiveIntegerField()),
                ('ordering', models.PositiveIntegerField()),
                ('nutrient', models.ForeignKey(to='food.Nutrient')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, editable=False, primary_key=True, unique=True, serialize=False, blank=True)),
                ('sequence', models.PositiveIntegerField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('description', models.TextField()),
                ('weight', models.DecimalField(decimal_places=2, max_digits=7)),
                ('deviation', models.DecimalField(decimal_places=3, default=0.0, max_digits=7)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together=set([('food', 'sequence')]),
        ),
        migrations.AlterUniqueTogether(
            name='nutrient',
            unique_together=set([('food', 'nutrient_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('food', 'factor_code')]),
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='food.FoodGroup'),
            preserve_default=True,
        ),
    ]
