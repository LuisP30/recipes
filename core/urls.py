from django.urls import path
from . import views

app_name = 'core'
# app para receitas (recipes), a tendência é que todas urls iniciem com "recipes" # noqa: E501, E261
# Exceção para a url da home que por opção ficou inclusa neste app. # noqa: E501, E261, E116
urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"), # noqa E261
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    # O termo "slug" se refere às URLs que descrevem o conteúdo que carregam.
]
