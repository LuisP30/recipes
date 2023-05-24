from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'global/index.html')

def cadastro(request):
    return HttpResponse('Cadastro')

def contato(request):
    return HttpResponse('Contato')
# Create your views here.
