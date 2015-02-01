# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
import timedelta.fields
import recipi.utils.db.uuid
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('calories', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('carbohydrate', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('protein', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('fat', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('saturated_fat', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('polyunsaturated_fat', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('monounsaturated_fat', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('trans_fat', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('cholesterol', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('sodium', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('potassium', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('fiber', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('sugar', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('vitamin_a', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('vitamin_b', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('vitamin_c', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('vitamin_d', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('calcium', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('iron', models.DecimalField(max_digits=6, default=0.0, decimal_places=2)),
                ('food', models.ForeignKey(blank=True, null=True, to='food.Food')),
                ('nutrients', models.ManyToManyField(to='food.Nutrient', null=True, blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, max_length=32, blank=True, primary_key=True, editable=False, unique=True)),
                ('url', models.URLField(max_length=2048, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('serving_description', models.TextField(blank=True)),
                ('steps', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('cook_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('metric_unit', models.CharField(max_length=3)),
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
            field=models.ManyToManyField(to='recipes.Ingredient', through='recipes.RecipeIngredient', related_name='recipes', blank=True),
            preserve_default=True,
        ),
    ]
