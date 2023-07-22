from django.test import TestCase
from core.models import Recipe, Category, User


class CoreTestBase(TestCase):

    def setUp(self) -> None:
        return super().setUp()

    def make_category(self, name='Category'):
        return Category.objects.create(name=name)
    def make_author(
            self,
            first_name='Luis',
            last_name='Henrique',
            username= 'luis',
            password='12345678',
            email='pimenta@gmail.com'
    ):
        return User.objects.create_user(
            first_name= first_name,
            last_name=last_name,
            username= username, # noqa
            password=password,
            email=email
        )
    def make_recipe(
        self,
        author_data = None, # noqa
        category_data = None, # noqa
        title = 'Recipe Title', # noqa
        description = 'Recipe Description', # noqa
        slug = 'recipe-slug', # noqa
        preparation_time = 10, # noqa
        preparation_time_unit = 'Minutos', # noqa
        servings = 5, # noqa
        servings_unit = 'Porções', # noqa
        preparation_steps = 'Recipe Preparation Steps', # noqa
        preparation_steps_is_html = False, # noqa
        is_published = True,  # noqa
    ):
        if category_data is None:
            category_data = {}
        if author_data is None:
            author_data = {}

        return Recipe.objects.create(
            author = self.make_author(**author_data), # noqa
            category = self.make_category(**category_data), # noqa
            title = title, # noqa
            description = description, # noqa
            slug = slug, # noqa
            preparation_time = preparation_time, # noqa
            preparation_time_unit = preparation_time_unit, # noqa
            servings = servings, # noqa
            servings_unit = servings_unit, # noqa
            preparation_steps = preparation_steps, # noqa
            preparation_steps_is_html = preparation_steps_is_html, # noqa
            is_published = is_published,  # noqa
        )
