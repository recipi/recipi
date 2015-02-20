# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import timedelta.fields
import djorm_pgarray.fields
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cuisine',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, primary_key=True, unique=True, blank=True, editable=False)),
                ('name', models.CharField(max_length=80)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('food', models.ForeignKey(null=True, to='food.Food', blank=True)),
                ('nutrients', models.ManyToManyField(to='food.Nutrient', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('file', models.ImageField(upload_to=None)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, primary_key=True, unique=True, blank=True, editable=False)),
                ('url', models.URLField(max_length=2048, blank=True)),
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
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('unit', models.CharField(choices=[('gram', 'gram'), ('clove', 'clove'), ('us gallon', 'gallon'), ('centiliter', 'centiliter'), ('drop', 'drop'), ('slice', 'slice'), ('ounce', 'ounce'), ('tablespoon', 'tablespoon'), ('teaspoon', 'teaspoon'), ('us fluid ounce', 'fluid ounce'), ('pound', 'pound'), ('kilogram', 'kilogram'), ('milligram', 'milligram'), ('package', 'package'), ('deciliter', 'deciliter'), ('milliliter', 'milliliter'), ('centigram', 'centigram'), ('us liquid pint', 'pint'), ('us liquid quart', 'quart'), ('bunch', 'bunch'), ('load', 'loaf'), ('cup', 'cup'), ('unknown', 'unknown'), ('carton', 'carton'), ('pinch', 'pinch'), ('can', 'can'), ('unit', 'unit'), ('liter', 'liter'), ('dash', 'dash')], max_length=3)),
                ('amount', models.PositiveIntegerField()),
                ('modifiers', models.TextField()),
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
