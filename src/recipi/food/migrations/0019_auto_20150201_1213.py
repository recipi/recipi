# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0018_auto_20150201_1212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='nutrientdefinition',
            name='nutrient_id',
            field=models.CharField(unique=True, max_length=3),
            preserve_default=True,
        ),
    ]
