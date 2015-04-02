# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.recipes.constants
import recipi.utils.db.uuid
import django.contrib.postgres.fields
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
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, primary_key=True, blank=True, serialize=False, max_length=32, editable=False)),
                ('name', models.CharField(max_length=80)),
            ],
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('name', models.CharField(max_length=256)),
                ('food', models.ForeignKey(to='food.Food', null=True, blank=True)),
                ('nutrients', models.ManyToManyField(to='food.Nutrient', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('file', models.ImageField(upload_to=None)),
            ],
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, primary_key=True, blank=True, serialize=False, max_length=32, editable=False)),
                ('url', models.URLField(max_length=2048, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('tags', django.contrib.postgres.fields.ArrayField(null=True, size=None, base_field=models.TextField(), blank=True)),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', models.DurationField()),
                ('cook_time', models.DurationField()),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(related_name='recipes', to='recipes.Cuisine', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('unit', models.CharField(choices=recipi.recipes.constants.get_unit_choices, max_length=3)),
                ('amount', models.PositiveIntegerField()),
                ('modifiers', models.TextField()),
                ('ingredient', models.ForeignKey(to='recipes.Ingredient')),
                ('recipe', models.ForeignKey(to='recipes.Recipe')),
            ],
        ),
        migrations.AddField(
            model_name='recipe',
            name='ingredients',
            field=models.ManyToManyField(related_name='recipes', through='recipes.RecipeIngredient', to='recipes.Ingredient', blank=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='pictures',
            field=models.ManyToManyField(related_name='recipes', to='recipes.Picture', blank=True),
        ),
    ]
