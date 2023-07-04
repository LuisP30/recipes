from django.contrib import admin
from .models import Category, Recipe

class CategoryAdmin(admin.ModelAdmin):
    ...

@admin.register(Recipe) # Uma forma de registro com decorator (registrando a classe Recipe)
class RecipeAdmin(admin.ModelAdmin):
    ...

admin.site.register(Category, CategoryAdmin) # Outra forma de registro (registrando a classe Category)