# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0004_auto_20150207_1302'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='tags',
            field=djorm_pgarray.fields.TextArrayField(dbtype='text'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='unit',
            field=models.CharField(max_length=3, choices=[('centiliter', 'centiliter'), ('kilogram', 'kilogram'), ('package', 'package'), ('liter', 'liter'), ('milligram', 'milligram'), ('can', 'can'), ('slice', 'slice'), ('dash', 'dash'), ('drop', 'drop'), ('us liquid pint', 'pint'), ('bunch', 'bunch'), ('centigram', 'centigram'), ('us liquid quart', 'quart'), ('load', 'loaf'), ('ounce', 'ounce'), ('pound', 'pound'), ('pinch', 'pinch'), ('milliliter', 'milliliter'), ('unit', 'unit'), ('us gallon', 'gallon'), ('cup', 'cup'), ('carton', 'carton'), ('teaspoon', 'teaspoon'), ('tablespoon', 'tablespoon'), ('gram', 'gram'), ('clove', 'clove'), ('deciliter', 'deciliter'), ('unknown', 'unknown'), ('us fluid ounce', 'fluid ounce')]),
            preserve_default=True,
        ),
    ]
