from django.shortcuts import render
from galeria.models import Livro

def index (request):
    livros = Livro.objects.all()
    return render(request,'galeria/index.html', {"cards":livros})

def imagem (request):
    return render(request, 'galeria/imagem.html')
