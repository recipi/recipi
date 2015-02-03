# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='calcium',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='calories',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='carbohydrate',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='cholesterol',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='fat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='fiber',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='iron',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='monounsaturated_fat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='polyunsaturated_fat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='potassium',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='protein',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='saturated_fat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='sodium',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='sugar',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='trans_fat',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='vitamin_a',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='vitamin_b',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='vitamin_c',
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='vitamin_d',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='serving_description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='steps',
        ),
        migrations.AddField(
            model_name='recipe',
            name='pictures',
            field=models.ManyToManyField(blank=True, to='recipes.Picture', related_name='recipes'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='recipeingredient',
            name='metric_unit',
            field=models.CharField(choices=[('milligram', 'milligram'), ('pinch', 'pinch'), ('liter', 'liter'), ('bunch', 'bunch'), ('clove', 'clove'), ('milliliter', 'milliliter'), ('deciliter', 'deciliter'), ('gram', 'gram'), ('ounce', 'ounce'), ('us liquid quart', 'quart'), ('drop', 'drop'), ('unknown', 'unknown'), ('kilogram', 'kilogram'), ('tablespoon', 'tablespoon'), ('can', 'can'), ('us gallon', 'gallon'), ('pound', 'pound'), ('load', 'loaf'), ('package', 'package'), ('unit', 'unit'), ('us fluid ounce', 'fluid ounce'), ('centigram', 'centigram'), ('carton', 'carton'), ('centiliter', 'centiliter'), ('dash', 'dash'), ('slice', 'slice'), ('teaspoon', 'teaspoon'), ('cup', 'cup'), ('us liquid pint', 'pint')], max_length=3),
            preserve_default=True,
        ),
    ]
