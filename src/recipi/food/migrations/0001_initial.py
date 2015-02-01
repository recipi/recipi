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
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('ndb_number', models.CharField(max_length=5)),
                ('name', models.TextField()),
                ('short_name', models.TextField()),
                ('scientific_name', models.TextField(blank=True)),
                ('common_names', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('manufacturer_name', models.TextField(blank=True)),
                ('survey', models.NullBooleanField(default=None)),
                ('refuse_description', models.TextField(blank=True)),
                ('refuse_percentage', models.PositiveIntegerField(blank=True, default=None, null=True)),
                ('nitrogen_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('protein_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('fat_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('carbohydrate_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
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
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('sequence', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=1, choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')])),
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
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
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
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('factor_code', models.CharField(max_length=5, unique=True)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('nutrient_id', models.CharField(max_length=3)),
                ('nutrient_value', models.DecimalField(max_digits=10, decimal_places=3)),
                ('unit', models.CharField(max_length=7)),
                ('description', models.CharField(max_length=60, blank=True)),
                ('decimal_places', models.PositiveIntegerField()),
                ('ordering', models.PositiveIntegerField()),
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
            name='Weight',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('sequence', models.PositiveIntegerField()),
                ('amount', models.DecimalField(max_digits=5, decimal_places=2)),
                ('description', models.TextField()),
                ('weight', models.DecimalField(max_digits=7, decimal_places=2)),
                ('deviation', models.DecimalField(max_digits=7, default=0.0, decimal_places=3)),
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
