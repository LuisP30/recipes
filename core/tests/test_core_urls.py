from django.test import TestCase
from django.urls import reverse

class CoreURLSTest(TestCase): # noqa E302
    def test_core_home_url_is_correct(self):
        url = reverse('core:home')
        self.assertEqual(url,'/') # noqa E251

    def test_core_category_url_is_correct(self):
        url = reverse('core:category', kwargs={'category_id': 1})
        self.assertEqual(url,'/recipes/category/1/') # noqa E251

    def test_core_recipe_url_is_correct(self):
        url = reverse('core:recipe', kwargs={'id': 1})
        self.assertEqual(url,'/recipes/1/') # noqa E251

    def test_core_search_url_is_correct(self):
        url = reverse('core:search')
        self.assertEqual(url,'/recipes/search/') # noqa E251
