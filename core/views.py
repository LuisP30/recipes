from django.shortcuts import render, get_list_or_404, get_object_or_404
from .models import Recipe
from django.http.response import Http404
from django.db.models import Q

#Função da página principal # noqa: E265
def home(request): # noqa: E302, E261
    recipes = Recipe.objects.filter(is_published = True).order_by('-id') # noqa: E501, E251, E261
    return render(request, 'recipes/pages/home.html', context={
        'recipes': recipes,
    })
#Essa função irá filtrar a categoria da receita. # noqa: E265
def category(request, category_id): # noqa: E302, E261
    recipes = get_list_or_404(
        Recipe.objects.filter(
        category__id=category_id, # noqa: E122, E261
        is_published=True # noqa: E122, E261
        ).order_by('-id'))
    return render(request, 'recipes/pages/category.html', context={
        'recipes': recipes,
        'title': f'{recipes[0].category.name} - Category'
    })
#Função da página de detalhes da receita # noqa: E265
def recipe(request, id): # noqa: E302, E261
    recipe = get_object_or_404(Recipe, pk = id, is_published = True) # noqa: E251, E261, E501
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
        Q(title__icontains=search_term) | 
        Q(description__icontains=search_term)
        ),
        is_published = True # noqa
        ).order_by('-id')
    return render(request, 'recipes/pages/search.html', {
        'page_title': f'Search for "{search_term}"',
        'search_term': search_term,
        'recipes': recipes,
    })
