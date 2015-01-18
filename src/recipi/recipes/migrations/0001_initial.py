# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
from django.conf import settings
import timedelta.fields
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('calories', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('carbohydrate', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('protein', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('fat', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('saturated_fat', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('polyunsaturated_fat', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('monounsaturated_fat', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('trans_fat', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('cholesterol', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('sodium', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('potassium', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('fiber', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('sugar', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('vitamin_a', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('vitamin_c', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('calcium', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
                ('iron', models.DecimalField(max_digits=6, decimal_places=2, default=0.0)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(primary_key=True, editable=False, serialize=False, unique=True, max_length=32, blank=True)),
                ('url', models.URLField(max_length=2048, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('serving_description', models.TextField(blank=True)),
                ('steps', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('cook_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(related_name='recipes', to='recipes.Cuisine', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('metric_unit', models.CharField(max_length=3, choices=[('mg', 'Milligram'), ('kg', 'Kilogram'), ('g', 'Gram'), ('sl', 'Slice')])),
                ('number', models.PositiveIntegerField()),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.RecipeIngredient', to='recipes.Ingredient', blank=True),
            preserve_default=True,
        ),
    ]
