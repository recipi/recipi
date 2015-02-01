# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0019_auto_20150201_1213'),
    ]

    operations = [
        migrations.AlterField(
            model_name='footnote',
            name='nutrient_id',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
