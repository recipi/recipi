import uuid

import pytest
from django.db.utils import DataError

from recipi.recipes.models import Recipe
from recipi.tests.factories.recipes import RecipeFactory


@pytest.mark.django_db
class TestRecipeModel:

    def setup(self):
        self.recipe = RecipeFactory.create()

    def test_has_title(self):
        assert self.recipe.title == 'Delicious Cookies'

    def test_title_has_maxlength(self):
        too_long = (
            'this text is simply too long to be good. '
            'Hell yeah, if a user enters this, we\'re doomed.'
        )

        with pytest.raises(DataError):
            RecipeFactory.create(title=too_long)

    def test_recipe_has_uuid_as_primary_key(self):
        recipe = RecipeFactory.create()

        # raises on invalid uuid
        uuid.UUID(str(recipe.pk))

    def test_recipe_can_have_tags(self):
        recipe = RecipeFactory.create()

        # defaults to empty list.
        assert recipe.tags is None

        recipe.tags = ['tag1', 'tag2']
        recipe.save()

        assert Recipe.objects.get(pk=recipe.pk).tags == ['tag1', 'tag2']
