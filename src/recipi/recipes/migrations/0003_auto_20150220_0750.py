# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150220_0747'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipeingredient',
            name='modifiers',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(choices=[('teaspoon', 'teaspoon'), ('centigram', 'centigram'), ('unknown', 'unknown'), ('carton', 'carton'), ('us liquid quart', 'quart'), ('drop', 'drop'), ('us fluid ounce', 'fluid ounce'), ('dash', 'dash'), ('milligram', 'milligram'), ('pound', 'pound'), ('liter', 'liter'), ('gram', 'gram'), ('centiliter', 'centiliter'), ('package', 'package'), ('cup', 'cup'), ('kilogram', 'kilogram'), ('ounce', 'ounce'), ('can', 'can'), ('deciliter', 'deciliter'), ('tablespoon', 'tablespoon'), ('us gallon', 'gallon'), ('pinch', 'pinch'), ('clove', 'clove'), ('load', 'loaf'), ('bunch', 'bunch'), ('milliliter', 'milliliter'), ('unit', 'unit'), ('slice', 'slice'), ('us liquid pint', 'pint')], max_length=3),
            preserve_default=True,
        ),
    ]
