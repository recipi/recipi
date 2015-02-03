# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timedelta.fields
from django.conf import settings
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('food', models.ForeignKey(to='food.Food', null=True, blank=True)),
                ('nutrients', models.ManyToManyField(blank=True, to='food.Nutrient', null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, unique=True, editable=False)),
                ('url', models.URLField(max_length=2048, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('cook_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(blank=True, to='recipes.Cuisine', related_name='recipes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('metric_unit', models.CharField(max_length=3, choices=[('can', 'can'), ('us gallon', 'gallon'), ('carton', 'carton'), ('unknown', 'unknown'), ('centiliter', 'centiliter'), ('bunch', 'bunch'), ('kilogram', 'kilogram'), ('cup', 'cup'), ('clove', 'clove'), ('us liquid pint', 'pint'), ('slice', 'slice'), ('us liquid quart', 'quart'), ('dash', 'dash'), ('pound', 'pound'), ('gram', 'gram'), ('drop', 'drop'), ('pinch', 'pinch'), ('milliliter', 'milliliter'), ('us fluid ounce', 'fluid ounce'), ('centigram', 'centigram'), ('load', 'loaf'), ('ounce', 'ounce'), ('tablespoon', 'tablespoon'), ('package', 'package'), ('milligram', 'milligram'), ('teaspoon', 'teaspoon'), ('liter', 'liter'), ('unit', 'unit'), ('deciliter', 'deciliter')])),
                ('volume', models.PositiveIntegerField()),
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
            field=models.ManyToManyField(blank=True, through='recipes.RecipeIngredient', to='recipes.Ingredient', related_name='recipes'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='recipes.Picture', related_name='recipes'),
            preserve_default=True,
        ),
    ]
