from django.urls import reverse, resolve
from core import views
from .test_core_base import CoreTestBase


class CoreSearchViewTest(CoreTestBase): # noqa E302

    def test_core_search_uses_correct_view_function(self):
        resolved = resolve(reverse('core:search'))
        self.assertIs(resolved.func, views.search)

    def test_core_search_loads_correct_template(self):
        response = self.client.get(reverse('core:search')+'?q=teste')
        self.assertTemplateUsed(response, 'recipes/pages/search.html')

    def test_core_search_raises_404_if_no_search_term(self):
        url = reverse('core:search')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)

    def test_core_search_term_is_on_page_title_and_escaped(self):
        url = reverse('core:search') + '?q=<Teste>'
        response = self.client.get(url)
        self.assertIn(
            'Search for &quot;&lt;Teste&gt;&quot;',
            response.content.decode('utf-8')
        )

        title1 = 'This is recipe one'
        title2 = 'This is recipe two'

        recipe1 = self.make_recipe(
            slug='one',
            title=title1,
            author_data={'username': 'one'}
        )
        recipe2 = self.make_recipe(
            slug='two',
            title=title2,
            author_data={'username': 'two'}
        )
        search_url = reverse('core:search')
        response1 = self.client.get(f'{search_url}?q={title1}')
        response2 = self.client.get(f'{search_url}?q={title2}')
        response_both = self.client.get(f'{search_url}?q=this')

        self.assertIn(recipe1, response1.context['recipes'])
        self.assertNotIn(recipe2, response1.context['recipes'])

        self.assertIn(recipe2, response2.context['recipes'])
        self.assertNotIn(recipe1, response2.context['recipes'])

        self.assertIn(recipe1, response_both.context['recipes'])
        self.assertIn(recipe2, response_both.context['recipes'])
