from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name="recipes-home"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),
]
