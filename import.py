import os
import csv
import codecs
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'recipi.settings')

import django
django.setup()

from recipi.food.models import FoodGroup


def get_reader(data, fieldnames):
    return csv.DictReader(data, fieldnames=fieldnames, delimiter='^', quotechar='~')


def import_food_groups(data):
    objects_updated, objects_created = 0, 0

    for row in get_reader(data, ('fdgr_cd', 'fdgr_desc')):
        print('Importing row {0}'.format(row))

        obj, created = FoodGroup.objects.update_or_create(
            code=row['fdgr_cd'],
            defaults={
                'name': row['fdgr_desc']
            }
        )

        if created:
            print('Created {0}'.format(repr(obj)))
            objects_created += 1
        else:
            print('Updated {0}'.format(repr(obj)))
            objects_updated += 1


    print('Created {0:d} new food groups'.format(objects_created))
    print('Updated {0:d} food groups'.format(objects_updated))


def import_usda(basepath):
    processors = {
        'FD_GROUP.txt': import_food_groups
    }

    for fname, handler in processors.items():
        with codecs.open(os.path.join(basepath, fname), encoding='cp1252') as fobj:
            handler(fobj)


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
    import_usda('./resources/')
    # recipes = import_recipes('recipeitems-latest.json')
    # print(len(recipes))
    # print(recipes[1])
