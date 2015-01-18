# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingredient',
            name='vitamin_b',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0.0),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='vitamin_d',
            field=models.DecimalField(decimal_places=2, max_digits=6, default=0.0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='metric_unit',
            field=models.CharField(max_length=3),
            preserve_default=True,
        ),
    ]
