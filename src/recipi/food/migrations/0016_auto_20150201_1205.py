# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0015_auto_20150201_1137'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='foonote',
            name='nutrient_number',
        ),
        migrations.AddField(
            model_name='foonote',
            name='food',
            field=models.ForeignKey(default=None, to='food.Food'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='foonote',
            name='nutrient_id',
            field=models.CharField(default=None, max_length=3, unique=True),
            preserve_default=False,
        ),
    ]
