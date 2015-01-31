# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0009_weight_sequence'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, unique=True, primary_key=True, editable=False, blank=True, serialize=False)),
                ('factor_code', models.CharField(max_length=5)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LanguageDescription',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(max_length=32, unique=True, primary_key=True, editable=False, blank=True, serialize=False)),
                ('factor_code', models.CharField(max_length=5)),
                ('description', models.TextField()),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('food', 'factor_code')]),
        ),
    ]
