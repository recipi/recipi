# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
        ('recipes', '0002_auto_20150118_2033'),
    ]

    operations = [
        migrations.RenameField(
            model_name='recipeingredient',
            old_name='number',
            new_name='volume',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.ForeignKey(blank=True, null=True, to='food.Food'),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='ingredient',
            name='nutrients',
            field=models.ManyToManyField(null=True, blank=True, to='food.Nutrient'),
            preserve_default=True,
        ),
    ]
