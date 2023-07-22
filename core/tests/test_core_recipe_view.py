from django.urls import reverse, resolve
from core import views
from .test_core_base import CoreTestBase

class CoreRecipeViewTest(CoreTestBase): # noqa E302
    def test_core_recipe_view_function_is_correct(self):
        view = resolve(reverse('core:recipe', kwargs={'id': 1}))
        self.assertIs(view.func, views.recipe)

    def test_core_recipe_view_returns_404_if_no_recipes_found(self):
        response = self.client.get(reverse('core:recipe', kwargs={'id': 1000})) # noqa E501
        self.assertEqual(response.status_code, 404)

    def test_core_recipe_template_loads_the_correct_recipe(self):
        needed_title = 'This is a recipe page - It load one recipe'
        self.make_recipe(title = needed_title) # noqa
        response = self.client.get(reverse('core:recipe', kwargs={'id': 1}))
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_core_recipe_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('core:recipe', kwargs={'id': recipe.id})) # noqa
        self.assertEqual(response.status_code, 404)
