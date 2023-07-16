from django.urls import reverse, resolve
from core import views
from .test_core_base import CoreTestBase


class CoreViewsTest(CoreTestBase): # noqa E302

    def test_core_home_view_function_is_correct(self):
        view = resolve(reverse('core:home'))
        self.assertIs(view.func, views.home)

    def test_core_home_view_returns_status_code_200_OK(self):
        response = self.client.get(reverse('core:home'))
        self.assertEqual(response.status_code, 200)

    def test_core_home_view_loads_correct_template(self):
        response = self.client.get(reverse('core:home'))
        self.assertTemplateUsed(response, 'recipes/pages/home.html')

    def test_core_home_template_shows_no_recipes_found_if_no_recipe(self):
        response = self.client.get(reverse('core:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))

    def test_core_home_template_loads_recipes(self):
        self.make_recipe()
        response = self.client.get(reverse('core:home'))
        content = response.content.decode('utf-8')
        response_context_recipes = response.context['recipes']
        self.assertIn('Recipe Title', content)
        self.assertEqual(len(response_context_recipes), 1)

    def test_core_home_template_dont_load_recipes_not_published(self):
        self.make_recipe(is_published=False)
        response = self.client.get(reverse('core:home'))
        self.assertIn('No recipes found', response.content.decode('utf-8'))

    def test_core_category_view_returns_404_if_no_recipes_found(self): # noqa
        response = self.client.get(reverse('core:category', kwargs={'category_id': 1000})) # noqa E501
        self.assertEqual(response.status_code, 404)

    def test_core_category_template_loads_recipes(self):
        needed_title = 'This is a category test'
        self.make_recipe(title = needed_title) # noqa
        response = self.client.get(reverse('core:category', args=(1,)))
        content = response.content.decode('utf-8')
        self.assertIn(needed_title, content)

    def test_core_category_template_dont_load_recipes_not_published(self):
        recipe = self.make_recipe(is_published=False)
        response = self.client.get(reverse('core:recipe', kwargs={'id': recipe.category.id})) # noqa
        self.assertEqual(response.status_code, 404)

    def test_core_category_view_function_is_correct(self):
        view = resolve(reverse('core:category', kwargs={'category_id': 1}))
        self.assertIs(view.func, views.category)

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
