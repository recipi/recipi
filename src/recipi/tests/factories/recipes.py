import factory

from recipi.recipes.models import Recipe, Ingredient
from recipi.tests.factories.accounts import UserFactory


class IngredientFactory(factory.DjangoModelFactory):

    class Meta:
        model = Ingredient


class RecipeFactory(factory.DjangoModelFactory):
    title = 'Delicious Cookies'

    author = factory.SubFactory(UserFactory)

    description = 'Hell yeah!'
    ingredients = factory.SubFactory(IngredientFactory)

    steps = [
        'Eat chocolate chips. They don\'t belong to others.',
        'Make dough. You know it\'s delicious.',
        'Hell, just eat the dough too. It\'s useless without chocolate chips.'
    ]

    servings = 1
    preparation_time = '2 hours'
    cook_time = '1 hour'

    class Meta:
        model = Recipe

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)

    @factory.post_generation
    def cuisines(self, create, extracted, **kwargs):
        if not create:
            return

        if extracted:
            for cuisine in extracted:
                self.cuisines.add(cuisine)
