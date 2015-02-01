import os
import csv
import codecs
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.settings')

import django
django.setup()

from recipi.food.models import (
    FoodGroup, Food, Language, LanguageDescription, Nutrient, Weight, Footnote
)


def _cl(string):
    return [x.strip() for x in string.split(',') if x.strip()]


def get_reader(data, fieldnames):
    return csv.DictReader(
        data, fieldnames=fieldnames, delimiter='^', quotechar='~')


def process_food_groups(data, verbose):
    objects_updated, objects_created = 0, 0

    for row in get_reader(data, ('fdgr_cd', 'fdgr_desc')):
        if verbose: print('Importing row {0}'.format(row))

        obj, created = FoodGroup.objects.update_or_create(
            code=row['fdgr_cd'],
            defaults={
                'name': row['fdgr_desc']
            }
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def process_food_description(data, verbose):
    objects_updated, objects_created = 0, 0

    fieldnames = (
        'ndb_no', 'fdgrp_cd', 'long_desc', 'short_desc', 'com_name',
        'manufac_name', 'survey', 'ref_desc', 'refuse', 'sci_name',
        'n_factor', 'pro_factor', 'fat_factor', 'cho_factor'
    )

    food_groups = {group.code: group for group in FoodGroup.objects.all()}

    for row in get_reader(data, fieldnames):
        if verbose: print('Importing row {0}'.format(row))

        survey = row.get('survey', None)

        obj, created = Food.objects.update_or_create(
            ndb_number=row['ndb_no'],
            defaults={
                'food_group': food_groups[row['fdgrp_cd']],
                'name': row['long_desc'],
                'short_name': row['short_desc'],
                'common_names': _cl(row.get('com_name', '')),
                'manufacturer_name': row.get('manufac_name', ''),
                'survey': survey == 'Y' if survey is not None else None,
                'refuse_description': row.get('ref_desc', ''),
                'refuse_percentage': int(row.get('refuse', 0) or 0),
                'scientific_name': row.get('scientific_name', ''),
                'nitrogen_factor': float(row.get('n_factor', 0.0) or 0.0),
                'protein_factor': float(row.get('pro_factor', 0.0) or 0.0),
                'fat_factor': float(row.get('fat_factor', 0.0) or 0.0),
                'carbohydrate_factor': float(row.get('cho_factor', 0.0) or 0.0),
            }
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def process_language(data, verbose):
    objects_updated, objects_created = 0, 0

    foods = {obj.ndb_number: obj for obj in Food.objects.all()}

    for row in get_reader(data, ('ndb_no', 'factor_code')):
        if verbose: print('Importing row {0}'.format(row))

        food = foods[row['ndb_no']]

        obj, created = Language.objects.update_or_create(
            food=food,
            factor_code=row['factor_code']
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def process_language_descriptions(data, verbose):
    objects_updated, objects_created = 0, 0

    for row in get_reader(data, ('factor_code', 'description')):
        if verbose: print('Importing row {0}'.format(row))

        obj, created = LanguageDescription.objects.update_or_create(
            factor_code=row['factor_code'],
            description=row['description'],
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def process_nutrient(basepath, verbose):
    objects_updated, objects_created = 0, 0
    foods = {obj.ndb_number: obj for obj in Food.objects.all()}

    # Get all nutrient definitions, we're storing all that information
    # in one table. This leads to some duplicate data
    # but is waaaay easier to access.
    definitions = {}

    with codecs.open(os.path.join(basepath, 'NUTR_DEF.txt'), encoding='cp1252') as fobj:

        fields = ('nutr_no', 'units', 'tagname', 'nutr_desc', 'num_desc', 'sr_order')

        for row in get_reader(fobj, fields):
            if verbose: print('Importing row {0}'.format(row))

            definitions[row['nutr_no']] = {
                'unit': row['units'],
                'description': row['nutr_desc'],
                'decimal_places': row['num_desc'],
                'ordering': row['sr_order']
            }

    fields = (
        'ndb_no', 'nutr_no', 'nutr_val', 'num_data_pts',
        'std_error', 'src_cd', 'deriv_cd', 'ref_ndb_no',
        'add_nutr_mark', 'num_studies', 'min', 'max', 'df',
        'low_eb', 'up_eb', 'stat_cmt', 'addmod_date', 'cc'
    )

    with codecs.open(os.path.join(basepath, 'NUT_DATA.txt'), encoding='cp1252') as fobj:
        for row in get_reader(fobj, fields):
            if verbose: print('Importing row {0}'.format(row))

            food = foods[row['ndb_no']]
            definition = definitions[row['nutr_no']]

            defaults = {
                'nutrient_value': float(row.get('nutr_val', 0.0) or 0.0),
                'min': float(row.get('min', 0.0) or 0.0),
                'max': float(row.get('max', 0.0) or 0.0),
                'degrees_of_freedon': int(row.get('df', 0) or 0),
                'lower_error_bound': float(row.get('low_eb', 0.0) or 0.0),
                'upper_error_bound': float(row.get('up_eb', 0.0) or 0.0),
            }

            defaults.update(definition)

            obj, created = Nutrient.objects.update_or_create(
                food=food,
                nutrient_id=row['nutr_no'],
                defaults=defaults
            )

            if created:
                if verbose: print('Created {0}'.format(repr(obj)))
                objects_created += 1
            else:
                if verbose: print('Updated {0}'.format(repr(obj)))
                objects_updated += 1

    return objects_created, objects_updated


def process_weight(data, verbose):
    objects_updated, objects_created = 0, 0
    foods = {obj.ndb_number: obj for obj in Food.objects.all()}

    fields = (
        'ndb_no', 'seq', 'amount', 'msre_desc', 'gm_wgt', 'num_data_pts',
        'std_dev'
    )

    for row in get_reader(data, fields):
        if verbose: print('Importing row {0}'.format(row))

        food = foods[row['ndb_no']]

        obj, created = Weight.objects.update_or_create(
            food=food,
            sequence=int(row['seq']),
            defaults={
                'amount': float(row['amount']),
                'description': row['msre_desc'],
                'weight': float(row['gm_wgt']),
                'deviation': float(row.get('std_dev', 0.0) or 0.0)
            }
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def process_footnote(data, verbose):
    objects_updated, objects_created = 0, 0
    foods = {obj.ndb_number: obj for obj in Food.objects.all()}

    fields = ('ndb_no', 'footnt_no', 'footnt_typ', 'nutr_no', 'footnt_txt')

    for row in get_reader(data, fields):
        if verbose: print('Importing row {0}'.format(row))

        food = foods[row['ndb_no']]

        obj, created = Footnote.objects.update_or_create(
            food=food,
            sequence=int(row['footnt_no']),
            type=row['footnt_typ'],
            nutrient_id=row['nutr_no'],
            defaults={
                'text': row['footnt_txt'],
            },
        )

        if created:
            if verbose: print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            if verbose: print('Updated {0}'.format(repr(obj)))
            objects_updated += 1

    return objects_created, objects_updated


def import_usda(basepath, verbose=True):
    # NOTE: processors are sorted!
    processors = (
        ('FD_GROUP.txt', process_food_groups, 'food groups'),
        ('FOOD_DES.txt', process_food_description, 'food descriptions'),
        ('LANGUAL.txt', process_language, 'language factors'),
        ('LANGDESC.txt', process_language_descriptions, 'language descriptions'),
        (None, process_nutrient, 'nutrient data'),
        ('WEIGHT.txt', process_weight, 'weight definitions'),
        ('FOOTNOTE.txt', process_footnote, 'footnotes'),
    )

    summary = []

    for fname, handler, description in processors:
        if fname is None:
            created, updated = handler(basepath, verbose)
        else:
            with codecs.open(os.path.join(basepath, fname), encoding='cp1252') as fobj:
                print('processing {0}'.format(description))
                created, updated = handler(fobj, verbose=verbose)

        summary.append(('Created {0:d} new {1}'.format(created, description)))
        summary.append(('Updated {0:d} {1}'.format(updated, description)))

    print('\n\n'.join(summary))



def import_recipes(fname):
    with codecs.open(fname, encoding='utf-8') as fobj:
        raw_data = fobj.read()

    recipes = []

    for line in raw_data.splitlines():

        try:
            parsed = json.loads(line.strip())
        except Exception:
            continue

        recipes.append({
            'name': parsed['name'],
            'source': parsed['source'],
            'url': parsed['url'],
            'recipe_yield': parsed.get('recipeYield', None),
            'ingredients': parsed['ingredients'].split('\n'),
            'prep_time': parsed.get('prepTime', None),
            'cook_time': parsed.get('cookTime', None),
            'published': parsed.get('datePublished', None),
            'description': parsed.get('description', None),
            'image': parsed.get('image', None)
        })

    return recipes


if __name__ == '__main__':
    import_usda('./resources/usda/')
    # recipes = import_recipes('recipeitems-latest.json')
    # print(len(recipes))
    # print(recipes[1])
