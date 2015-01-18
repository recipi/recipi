import pytest
from django.db.utils import DataError

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
