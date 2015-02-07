# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0002_auto_20150206_1938'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='volume',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='metric_unit',
            field=models.CharField(choices=[('carton', 'carton'), ('package', 'package'), ('gram', 'gram'), ('teaspoon', 'teaspoon'), ('centigram', 'centigram'), ('can', 'can'), ('unit', 'unit'), ('milliliter', 'milliliter'), ('load', 'loaf'), ('centiliter', 'centiliter'), ('kilogram', 'kilogram'), ('pinch', 'pinch'), ('slice', 'slice'), ('milligram', 'milligram'), ('tablespoon', 'tablespoon'), ('drop', 'drop'), ('dash', 'dash'), ('cup', 'cup'), ('us liquid pint', 'pint'), ('unknown', 'unknown'), ('liter', 'liter'), ('ounce', 'ounce'), ('pound', 'pound'), ('us liquid quart', 'quart'), ('bunch', 'bunch'), ('us gallon', 'gallon'), ('deciliter', 'deciliter'), ('us fluid ounce', 'fluid ounce'), ('clove', 'clove')], max_length=3),
            preserve_default=True,
        ),
    ]
