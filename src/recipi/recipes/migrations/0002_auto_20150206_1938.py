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
            name='metric_unit',
            field=models.CharField(choices=[('liter', 'liter'), ('kilogram', 'kilogram'), ('milliliter', 'milliliter'), ('tablespoon', 'tablespoon'), ('gram', 'gram'), ('can', 'can'), ('unit', 'unit'), ('ounce', 'ounce'), ('milligram', 'milligram'), ('pound', 'pound'), ('bunch', 'bunch'), ('us gallon', 'gallon'), ('centigram', 'centigram'), ('slice', 'slice'), ('cup', 'cup'), ('drop', 'drop'), ('deciliter', 'deciliter'), ('unknown', 'unknown'), ('centiliter', 'centiliter'), ('carton', 'carton'), ('pinch', 'pinch'), ('teaspoon', 'teaspoon'), ('dash', 'dash'), ('us liquid pint', 'pint'), ('us fluid ounce', 'fluid ounce'), ('us liquid quart', 'quart'), ('package', 'package'), ('load', 'loaf'), ('clove', 'clove')], max_length=3),
            preserve_default=True,
        ),
    ]
