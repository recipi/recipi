from django.db import models
from timedelta import fields as timedelta_fields
from djorm_pgarray.fields import TextArrayField

from recipi.recipes.constants import UNIT_CHOICES
from recipi.utils.db.uuid import UUIDField
from recipi.utils.files import upload_to


class Ingredient(models.Model):
    name = models.CharField(max_length=256)
    food = models.ForeignKey('food.Food', null=True, blank=True)
    nutrients = models.ManyToManyField('food.Nutrient', null=True, blank=True)


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey('Recipe')
    ingredient = models.ForeignKey(Ingredient)

    unit = models.CharField(max_length=3, choices=UNIT_CHOICES)
    amount = models.PositiveIntegerField()

    # Modifiers such as 'chopped' or 'fresh' etc.
    modifiers = models.TextField()


class Cuisine(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    name = models.CharField(max_length=80)


class Picture(models.Model):
    file = models.ImageField(upload_to=upload_to('recipes/pictures/%S/%W/{0}/{1}'))


class Recipe(models.Model):
    id = UUIDField(auto=True, primary_key=True)
    url = models.URLField(max_length=2048, blank=True)

    title = models.CharField(max_length=80)

    author = models.ForeignKey('accounts.User')

    description = models.TextField(blank=True)

    ingredients = models.ManyToManyField(
        Ingredient,
        related_name='recipes',
        through='RecipeIngredient',
        blank=True
    )

    cuisines = models.ManyToManyField(
        Cuisine,
        related_name='recipes',
        blank=True
    )

    pictures = models.ManyToManyField(
        Picture,
        related_name='recipes',
        blank=True
    )

    tags = TextArrayField(null=True, blank=True)

    # We're always talking about a one serving per 'Person' here.
    servings = models.PositiveIntegerField()

    preparation_time = timedelta_fields.TimedeltaField()
    cook_time = timedelta_fields.TimedeltaField()
