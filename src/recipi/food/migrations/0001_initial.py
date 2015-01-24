# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FoodDescription',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, blank=True, primary_key=True, max_length=32, serialize=False, editable=False)),
                ('ndb_no', models.CharField(max_length=5)),
                ('food_group', models.CharField(max_length=4)),
                ('long_description', models.TextField()),
                ('short_description', models.TextField()),
                ('common_names', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('survey', models.BooleanField(default=False)),
                ('refuse_description', models.TextField(blank=True)),
                ('refuse', models.PositiveIntegerField(null=True, default=None, blank=True)),
                ('scientific_name', models.TextField(blank=True)),
                ('nitrogen_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('protein_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('fat_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
                ('carbohydrate_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
