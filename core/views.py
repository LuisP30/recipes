from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
from django.http.response import Http404
from django.db.models import Q
from utils.pagination import make_pagination
import os


PER_PAGE = int(os.environ.get('PER_PAGE', 6))  # Número de receitas por página


def home(request):
    recipes = Recipe.objects.filter(is_published=True).order_by('-id')
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/home.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
    })

def category(request, category_id):  # Essa função irá filtrar a categoria da receita. # noqa
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category__id=category_id, # noqa
        is_published=True # noqa
        ).order_by('-id'))
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/category.html', context={
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'title': f'{recipes[0].category.name} - Category'
    })


def recipe(request, id):  # Função da página de detalhes da receita
    recipe = get_object_or_404(Recipe, pk = id, is_published = True) # noqa
    return render(request, 'recipes/pages/recipe-view.html', context={
        'recipe': recipe,
        'is_detail_page': True
    })


def search(request):
    search_term = request.GET.get('q', '').strip()
    if not search_term:
        raise Http404()
# Aqui estou adicionando funcionalidade a barra search # noqa
    recipes = Recipe.objects.filter(
        Q(
        Q(title__icontains=search_term) |           # noqa
        Q(description__icontains=search_term)       # noqa
        ),
        is_published = True # noqa
        ).order_by('-id')
    page_obj, pagination_range = make_pagination(request, recipes, PER_PAGE)
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': page_obj,
        'pagination_range': pagination_range,
        'additional_url_query': f'&q={search_term}',
    })
