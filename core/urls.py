from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/', views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
    # O termo "slug" se refere às URLs que descrevem o conteúdo que carregam.
]
