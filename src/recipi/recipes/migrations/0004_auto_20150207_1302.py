# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0003_auto_20150207_1302'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipeingredient',
            name='metric_unit',
        ),
        migrations.AddField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(default=None, choices=[('us liquid quart', 'quart'), ('pinch', 'pinch'), ('cup', 'cup'), ('unit', 'unit'), ('pound', 'pound'), ('load', 'loaf'), ('slice', 'slice'), ('unknown', 'unknown'), ('can', 'can'), ('us liquid pint', 'pint'), ('kilogram', 'kilogram'), ('us fluid ounce', 'fluid ounce'), ('deciliter', 'deciliter'), ('teaspoon', 'teaspoon'), ('drop', 'drop'), ('ounce', 'ounce'), ('clove', 'clove'), ('milligram', 'milligram'), ('tablespoon', 'tablespoon'), ('package', 'package'), ('milliliter', 'milliliter'), ('centigram', 'centigram'), ('liter', 'liter'), ('us gallon', 'gallon'), ('gram', 'gram'), ('centiliter', 'centiliter'), ('bunch', 'bunch'), ('dash', 'dash'), ('carton', 'carton')], max_length=3),
            preserve_default=False,
        ),
    ]
