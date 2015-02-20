# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import timedelta.fields
import recipi.utils.db.uuid
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, primary_key=True, max_length=32, blank=True, serialize=False, editable=False)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=256)),
                ('food', models.ForeignKey(null=True, to='food.Food', blank=True)),
                ('nutrients', models.ManyToManyField(null=True, to='food.Nutrient', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, primary_key=True, max_length=32, blank=True, serialize=False, editable=False)),
                ('url', models.URLField(blank=True, max_length=2048)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('tags', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField()),
                ('cook_time', timedelta.fields.TimedeltaField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(to='recipes.Cuisine', related_name='recipes', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('unit', models.CharField(choices=[('centigram', 'centigram'), ('dash', 'dash'), ('centiliter', 'centiliter'), ('clove', 'clove'), ('milligram', 'milligram'), ('milliliter', 'milliliter'), ('gram', 'gram'), ('drop', 'drop'), ('pinch', 'pinch'), ('deciliter', 'deciliter'), ('kilogram', 'kilogram'), ('carton', 'carton'), ('cup', 'cup'), ('tablespoon', 'tablespoon'), ('pound', 'pound'), ('us liquid pint', 'pint'), ('bunch', 'bunch'), ('us fluid ounce', 'fluid ounce'), ('slice', 'slice'), ('unit', 'unit'), ('us gallon', 'gallon'), ('package', 'package'), ('can', 'can'), ('us liquid quart', 'quart'), ('unknown', 'unknown'), ('load', 'loaf'), ('teaspoon', 'teaspoon'), ('liter', 'liter'), ('ounce', 'ounce')], max_length=3)),
                ('amount', models.PositiveIntegerField()),
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
            field=models.ManyToManyField(through='recipes.RecipeIngredient', to='recipes.Ingredient', related_name='recipes', blank=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='recipe',
            name='pictures',
            field=models.ManyToManyField(to='recipes.Picture', related_name='recipes', blank=True),
            preserve_default=True,
        ),
    ]
