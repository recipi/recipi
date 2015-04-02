# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import recipi.utils.db.uuid
import django.contrib.postgres.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('ndb_number', models.CharField(serialize=False, help_text='5-digit nutrient databank number that uniquely identifies a food item.', max_length=5, primary_key=True, verbose_name='NDB Number')),
                ('name', models.TextField(help_text='of this food item', verbose_name='Name')),
                ('short_name', models.TextField(help_text='abbreviated name of this food item.', verbose_name='Short Name')),
                ('scientific_name', models.TextField(help_text='scientific name of the food item. Given for the least processed for most food (usually raw), if applicable.', blank=True, verbose_name='Scientific Name')),
                ('common_names', django.contrib.postgres.fields.ArrayField(help_text='Other names commonly used to describe this item. For example "soda" or "pop" for "carbonated beverages".', base_field=models.TextField(), blank=True, size=None, verbose_name='Common Names')),
                ('manufacturer_name', models.TextField(blank=True, verbose_name='Manufacturer Name')),
                ('survey', models.NullBooleanField(default=None, verbose_name='Has Survey?', help_text='Indicates if the food item is used in the USDA Food and Nutrient Database for Dietary Studies (FNDDS) and thus has a complete nutrient profile for the 65 FNDDS nutrients.')),
                ('refuse_description', models.TextField(help_text='Description of inedible parts of a food item (refuse), such as seeds or bone.', blank=True, verbose_name='Refuse Description')),
                ('refuse_percentage', models.PositiveIntegerField(null=True, default=None, blank=True, verbose_name='Percentage of refuse')),
                ('nitrogen_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2, help_text='Factor for converting nitrogen to protein', verbose_name='Nitrogen Factor')),
                ('protein_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2, help_text='Factor for calculating calories from protein', verbose_name='Protein Factor')),
                ('fat_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2, help_text='Factor for calculating calories from fat', verbose_name='Fat Factor')),
                ('carbohydrate_factor', models.DecimalField(default=0.0, max_digits=4, decimal_places=2, help_text='Factor for calculating calories from carbohydrate', verbose_name='Carbohydrate Factor')),
            ],
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('code', models.CharField(serialize=False, help_text='4-digit code identifying a food group. Only the first 2 digits are currently assigned.', max_length=4, primary_key=True, verbose_name='Code')),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, max_length=32, blank=True, serialize=False, primary_key=True, editable=False)),
                ('sequence', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=1, choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')])),
                ('nutrient_id', models.CharField(max_length=3)),
                ('text', models.TextField()),
                ('food', models.ForeignKey(to='food.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, max_length=32, blank=True, serialize=False, primary_key=True, editable=False)),
                ('factor_code', models.CharField(help_text='The LanguaL factor from the Thesaurus', max_length=5, verbose_name='Factor Code')),
                ('food', models.ForeignKey(to='food.Food')),
            ],
        ),
        migrations.CreateModel(
            name='LanguageDescription',
            fields=[
                ('factor_code', models.CharField(serialize=False, primary_key=True, max_length=5, verbose_name='Factor Code')),
                ('description', models.TextField(verbose_name='Description')),
            ],
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, max_length=32, blank=True, serialize=False, primary_key=True, editable=False)),
                ('nutrient_id', models.CharField(max_length=3, verbose_name='Nutrient ID')),
                ('name', models.CharField(max_length=60, blank=True, verbose_name='Name')),
                ('nutrient_value', models.DecimalField(help_text='Amount in 100 grams, edible portion †.', max_digits=10, decimal_places=3, verbose_name='Nutrient Value')),
                ('unit', models.CharField(help_text='Units of measure (mg, g, μg, etc)', max_length=7, verbose_name='Unit')),
                ('decimal_places', models.PositiveIntegerField(help_text='Number of decimal places to which a nutrient value is rounded.', verbose_name='Decimal Places')),
                ('ordering', models.PositiveIntegerField(help_text='Used for correct ordering in nutrition information.', verbose_name='Ordering')),
                ('min', models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Min')),
                ('max', models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Max')),
                ('degrees_of_freedom', models.PositiveIntegerField(verbose_name='Degrees of Freedom')),
                ('lower_error_bound', models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Lower Error Bound')),
                ('upper_error_bound', models.DecimalField(max_digits=10, decimal_places=3, verbose_name='Upper Error Bound')),
                ('food', models.ForeignKey(to='food.Food')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(unique=True, max_length=32, blank=True, serialize=False, primary_key=True, editable=False)),
                ('sequence', models.PositiveIntegerField(verbose_name='Sequence')),
                ('amount', models.DecimalField(help_text='Unit modifier (for example 1 in "1 cup")', max_digits=5, decimal_places=2, verbose_name='Amount')),
                ('description', models.TextField(help_text='Description (for example, cup, diced, and 1-inch pieces)', verbose_name='Description')),
                ('weight', models.DecimalField(help_text='Weight in gram', max_digits=7, decimal_places=2, verbose_name='Weight')),
                ('deviation', models.DecimalField(default=0.0, max_digits=7, decimal_places=3, help_text='Standard deviation', verbose_name='Deviation')),
                ('food', models.ForeignKey(to='food.Food')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(to='food.FoodGroup', verbose_name='Food Group'),
        ),
        migrations.AlterUniqueTogether(
            name='weight',
            unique_together=set([('food', 'sequence')]),
        ),
        migrations.AlterUniqueTogether(
            name='nutrient',
            unique_together=set([('food', 'nutrient_id')]),
        ),
        migrations.AlterUniqueTogether(
            name='language',
            unique_together=set([('food', 'factor_code')]),
        ),
    ]
