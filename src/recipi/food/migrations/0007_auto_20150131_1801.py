# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0006_auto_20150131_1800'),
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(primary_key=True, editable=False, serialize=False, max_length=32, blank=True, unique=True)),
                ('ndb_number', models.CharField(max_length=5)),
                ('long_description', models.TextField()),
                ('short_description', models.TextField()),
                ('common_names', djorm_pgarray.fields.TextArrayField(dbtype='text')),
                ('manufacturer_name', models.TextField(blank=True)),
                ('survey', models.NullBooleanField(default=None)),
                ('refuse_description', models.TextField(blank=True)),
                ('refuse_percentage', models.PositiveIntegerField(blank=True, null=True, default=None)),
                ('scientific_name', models.TextField(blank=True)),
                ('nitrogen_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('protein_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('fat_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('carbohydrate_factor', models.DecimalField(max_digits=4, default=0.0, decimal_places=2)),
                ('food_group', models.ForeignKey(to='food.FoodGroup')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='fooddescription',
            name='food_group',
        ),
        migrations.AlterField(
            model_name='weight',
            name='food',
            field=models.ForeignKey(to='food.Food'),
            preserve_default=True,
        ),
        migrations.DeleteModel(
            name='FoodDescription',
        ),
    ]
