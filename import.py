import os
import csv
import codecs
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.settings')

import django
django.setup()

from recipi.food.models import FoodGroup, Food, Language, LanguageDescription


def _cl(string):
    return [x.strip() for x in string.split(',')]


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


def import_usda(basepath, verbose=False):
    # NOTE: processors are sorted!
    processors = (
        ('FD_GROUP.txt', process_food_groups, 'food groups'),
        ('FOOD_DES.txt', process_food_description, 'food descriptions'),
        ('LANGUAL.txt', process_language, 'language factors'),
    )

    for fname, handler, description in processors:
        if fname is None:
            handler(basepath)
        else:
            with codecs.open(os.path.join(basepath, fname), encoding='cp1252') as fobj:
                print('processing {0}'.format(description))
                created, updated = handler(fobj, verbose=verbose)
                print('Created {0:d} new {1}'.format(created, description))
                print('Updated {0:d} {1}'.format(updated, description))



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
