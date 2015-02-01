# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0016_auto_20150201_1205'),
    ]

    operations = [
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(editable=False, primary_key=True, max_length=32, unique=True, serialize=False, blank=True)),
                ('sequence', models.PositiveIntegerField()),
                ('type', models.CharField(choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')], max_length=1)),
                ('nutrient_id', models.CharField(unique=True, max_length=3)),
                ('text', models.TextField()),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='foonote',
            name='food',
        ),
        migrations.DeleteModel(
            name='Foonote',
        ),
    ]
