from django.urls import reverse, resolve
from core import views
from .test_core_base import CoreTestBase


class CoreCategoryViewTest(CoreTestBase): # noqa E302


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