from .test_core_base import CoreTestBase, Recipe
from django.core.exceptions import ValidationError
from parameterized import parameterized


class RecipeModelTest(CoreTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()

    def make_recipe_no_defaults(self):
        recipe = Recipe(
            author = self.make_author(username='newuser'), # noqa
            category = self.make_category(name='Test Default Category'), # noqa
            title = 'Recipe Title', # noqa
            description = 'Recipe Description', # noqa
            slug = 'recipe-slug-for-no-defaults', # noqa
            preparation_time = 10, # noqa
            preparation_time_unit = 'Minutos', # noqa
            servings = 5, # noqa
            servings_unit = 'Porções', # noqa
            preparation_steps = 'Recipe Preparation Steps', # noqa
        )
        recipe.full_clean()
        recipe.save()
        return recipe

    def test_recipe_title_raises_error_if_title_has_more_than_65_chars(self):
        self.recipe.title = 'A' * 70  # O título aceita no máximo 65 caracteres

    @parameterized.expand([
            ('title', 65),
            ('description', 165),
            ('preparation_time_unit', 65),
            ('servings_unit', 65)
    ])
    def test_recipe_fields_max_length(self, field, max_length):
        setattr(self.recipe, field, 'A' * (max_length + 1))
        with self.assertRaises(ValidationError):
            self.recipe.full_clean()

    def test_recipe_preparation_steps_is_html_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.preparation_steps_is_html,
            msg='Recipe preparation_steps_is_html não está com valor padrão False' # noqa
        )

    def test_recipe_is_published_is_false_by_default(self):
        recipe = self.make_recipe_no_defaults()
        self.assertFalse(
            recipe.is_published,
            msg='Recipe is_published não está com valor padrão False'
        )
    def test_recipe_string_representation(self):
        needed = 'Testing Representation'
        self.recipe.title = 'Testing Representation'
        self.recipe.full_clean()
        self.recipe.save()
        self.assertEqual(str(self.recipe), needed,
            msg = f'Recipe string representation must be "{needed}"')
