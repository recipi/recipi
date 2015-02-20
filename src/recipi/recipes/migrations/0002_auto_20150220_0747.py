# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=3, choices=[('drop', 'drop'), ('dash', 'dash'), ('teaspoon', 'teaspoon'), ('kilogram', 'kilogram'), ('centigram', 'centigram'), ('carton', 'carton'), ('milliliter', 'milliliter'), ('pinch', 'pinch'), ('liter', 'liter'), ('clove', 'clove'), ('centiliter', 'centiliter'), ('gram', 'gram'), ('package', 'package'), ('pound', 'pound'), ('bunch', 'bunch'), ('us liquid quart', 'quart'), ('slice', 'slice'), ('tablespoon', 'tablespoon'), ('us liquid pint', 'pint'), ('can', 'can'), ('deciliter', 'deciliter'), ('unknown', 'unknown'), ('unit', 'unit'), ('us fluid ounce', 'fluid ounce'), ('ounce', 'ounce'), ('us gallon', 'gallon'), ('milligram', 'milligram'), ('cup', 'cup'), ('load', 'loaf')]),
            preserve_default=True,
        ),
    ]
