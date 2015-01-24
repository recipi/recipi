# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(primary_key=True, editable=False, blank=True, unique=True, max_length=32, serialize=False)),
                ('code', models.CharField(max_length=4)),
                ('name', models.CharField(max_length=60)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='fooddescription',
            name='food_group',
            field=models.ForeignKey(to='food.FoodGroup'),
            preserve_default=True,
        ),
    ]
