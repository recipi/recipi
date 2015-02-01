# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
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
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
                ('food', models.ForeignKey(to='food.Food', null=True, blank=True)),
                ('nutrients', models.ManyToManyField(to='food.Nutrient', blank=True, null=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, serialize=False, unique=True, blank=True, primary_key=True, editable=False)),
                ('url', models.URLField(max_length=2048, blank=True)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField(blank=True)),
                ('serving_description', models.TextField(blank=True)),
                ('steps', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField(min_value=None, max_value=None)),
                ('cook_time', timedelta.fields.TimedeltaField(min_value=None, max_value=None)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(blank=True, related_name='recipes', to='recipes.Cuisine')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='RecipeIngredient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
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
            field=models.ManyToManyField(through='recipes.RecipeIngredient', blank=True, related_name='recipes', to='recipes.Ingredient'),
            preserve_default=True,
        ),
    ]
