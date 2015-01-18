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
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(blank=True, primary_key=True, editable=False, max_length=32, unique=True, serialize=False)),
                ('url', models.URLField(blank=True, max_length=2048)),
                ('title', models.CharField(max_length=80)),
                ('description', models.TextField()),
                ('steps', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('servings', models.PositiveIntegerField()),
                ('preparation_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('cook_time', timedelta.fields.TimedeltaField(max_value=None, min_value=None)),
                ('author', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
                ('cuisines', models.ManyToManyField(blank=True, to='recipes.Cuisine', related_name='recipes')),
                ('ingredients', models.ManyToManyField(blank=True, to='recipes.Ingredient', related_name='recipes')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
