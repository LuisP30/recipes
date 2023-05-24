from django.urls import path
from core.views import home, cadastro, contato

urlpatterns = [
    path('', home),
    path('cadastro/', cadastro),
    path('contato/', contato),
]
