from .test_core_base import CoreTestBase


class RecipeModelTest(CoreTestBase):
    def setUp(self) -> None:
        self.recipe = self.make_recipe()
        return super().setUp()
