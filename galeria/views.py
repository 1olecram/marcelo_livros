from django.shortcuts import render,get_object_or_404
from galeria.models import Livro

def index (request):
    livros = Livro.objects.order_by("data_adicao_livro").filter(publicado=True)
    return render(request,'galeria/index.html', {"cards":livros})

def imagem (request,foto_id):
    livro = get_object_or_404(Livro, pk = foto_id)
    return render(request, 'galeria/imagem.html',{"livro":livro})
