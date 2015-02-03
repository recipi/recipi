# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import djorm_pgarray.fields
import recipi.utils.db.uuid


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('ndb_number', models.CharField(primary_key=True, verbose_name='NDB Number', help_text='5-digit nutrient databank number that uniquely identifies a food item.', serialize=False, max_length=5)),
                ('name', models.TextField(verbose_name='Name', help_text='of this food item')),
                ('short_name', models.TextField(verbose_name='Short Name', help_text='abbreviated name of this food item.')),
                ('scientific_name', models.TextField(blank=True, verbose_name='Scientific Name', help_text='scientific name of the food item. Given for the least processed for most food (usually raw), if applicable.')),
                ('common_names', djorm_pgarray.fields.TextArrayField(verbose_name='Common Names', help_text='Other names commonly used to describe this item. For example "soda" or "pop" for "carbonated beverages".', dbtype='text')),
                ('manufacturer_name', models.TextField(blank=True, verbose_name='Manufacturer Name')),
                ('survey', models.NullBooleanField(verbose_name='Has Survey?', help_text='Indicates if the food item is used in the USDA Food and Nutrient Database for Dietary Studies (FNDDS) and thus has a complete nutrient profile for the 65 FNDDS nutrients.', default=None)),
                ('refuse_description', models.TextField(blank=True, verbose_name='Refuse Description', help_text='Description of inedible parts of a food item (refuse), such as seeds or bone.')),
                ('refuse_percentage', models.PositiveIntegerField(blank=True, verbose_name='Percentage of refuse', default=None, null=True)),
                ('nitrogen_factor', models.DecimalField(verbose_name='Nitrogen Factor', help_text='Factor for converting nitrogen to protein', default=0.0, decimal_places=2, max_digits=4)),
                ('protein_factor', models.DecimalField(verbose_name='Protein Factor', help_text='Factor for calculating calories from protein', default=0.0, decimal_places=2, max_digits=4)),
                ('fat_factor', models.DecimalField(verbose_name='Fat Factor', help_text='Factor for calculating calories from fat', default=0.0, decimal_places=2, max_digits=4)),
                ('carbohydrate_factor', models.DecimalField(verbose_name='Carbohydrate Factor', help_text='Factor for calculating calories from carbohydrate', default=0.0, decimal_places=2, max_digits=4)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='FoodGroup',
            fields=[
                ('code', models.CharField(primary_key=True, verbose_name='Code', help_text='4-digit code identifying a food group. Only the first 2 digits are currently assigned.', serialize=False, max_length=4)),
                ('name', models.CharField(max_length=60, verbose_name='Name')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Footnote',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, unique=True, editable=False)),
                ('sequence', models.PositiveIntegerField()),
                ('type', models.CharField(max_length=1, choices=[('D', 'Food '), ('M', 'Measure'), ('N', 'Nutrient')])),
                ('nutrient_id', models.CharField(max_length=3)),
                ('text', models.TextField()),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, unique=True, editable=False)),
                ('factor_code', models.CharField(max_length=5, verbose_name='Factor Code', help_text='The LanguaL factor from the Thesaurus')),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='LanguageDescription',
            fields=[
                ('factor_code', models.CharField(primary_key=True, verbose_name='Factor Code', serialize=False, max_length=5)),
                ('description', models.TextField(verbose_name='Description')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, unique=True, editable=False)),
                ('nutrient_id', models.CharField(max_length=3, verbose_name='Nutrient ID')),
                ('name', models.CharField(max_length=60, verbose_name='Name', blank=True)),
                ('nutrient_value', models.DecimalField(verbose_name='Nutrient Value', help_text='Amount in 100 grams, edible portion †.', decimal_places=3, max_digits=10)),
                ('unit', models.CharField(max_length=7, verbose_name='Unit', help_text='Units of measure (mg, g, μg, etc)')),
                ('decimal_places', models.PositiveIntegerField(verbose_name='Decimal Places', help_text='Number of decimal places to which a nutrient value is rounded.')),
                ('ordering', models.PositiveIntegerField(verbose_name='Ordering', help_text='Used for correct ordering in nutrition information.')),
                ('min', models.DecimalField(verbose_name='Min', decimal_places=3, max_digits=10)),
                ('max', models.DecimalField(verbose_name='Max', decimal_places=3, max_digits=10)),
                ('degrees_of_freedom', models.PositiveIntegerField(verbose_name='Degrees of Freedom')),
                ('lower_error_bound', models.DecimalField(verbose_name='Lower Error Bound', decimal_places=3, max_digits=10)),
                ('upper_error_bound', models.DecimalField(verbose_name='Upper Error Bound', decimal_places=3, max_digits=10)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', recipi.utils.db.uuid.UUIDField(serialize=False, primary_key=True, max_length=32, blank=True, unique=True, editable=False)),
                ('sequence', models.PositiveIntegerField(verbose_name='Sequence')),
                ('amount', models.DecimalField(verbose_name='Amount', help_text='Unit modifier (for example 1 in "1 cup")', decimal_places=2, max_digits=5)),
                ('description', models.TextField(verbose_name='Description', help_text='Description (for example, cup, diced, and 1-inch pieces)')),
                ('weight', models.DecimalField(verbose_name='Weight', help_text='Weight in gram', decimal_places=2, max_digits=7)),
                ('deviation', models.DecimalField(verbose_name='Deviation', help_text='Standard deviation', default=0.0, decimal_places=3, max_digits=7)),
                ('food', models.ForeignKey(to='food.Food')),
            ],
            options={
            },
            bases=(models.Model,),
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
        migrations.AddField(
            model_name='food',
            name='food_group',
            field=models.ForeignKey(verbose_name='Food Group', to='food.FoodGroup'),
            preserve_default=True,
        ),
    ]
