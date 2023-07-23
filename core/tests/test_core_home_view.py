
from django.urls import reverse, resolve
from core import views
from .test_core_base import CoreTestBase
from unittest.mock import patch

class CoreHomeViewTest(CoreTestBase): # noqa E302

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


    def test_core_home_is_paginated(self):
        for i in range(9):
            kwargs = {'slug': f'r{i}', 'author_data': {'username': f'u{i}'}}
            self.make_recipe(**kwargs)

        with patch('core.views.PER_PAGE', new=3):
            response = self.client.get(reverse('core:home'))
            recipes = response.context['recipes']
            paginator = recipes.paginator
            self.assertEqual(paginator.num_pages, 3)
            self.assertEqual(len(paginator.get_page(1)), 3)
            self.assertEqual(len(paginator.get_page(2)), 3)
            self.assertEqual(len(paginator.get_page(3)), 3)