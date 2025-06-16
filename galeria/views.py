from django.shortcuts import render



def index (request):
    dados = {
    1:{"nome":"Ganbatte", "legenda":"Nobuo Suzuki / 2022 / Sextante"},
    2:{"nome":"Essencialismo", "legenda":"Greg McKeown / 2015 / Sextante"}
}
    return render(request,'galeria/index.html', {"cards":dados})

def imagem (request):
    return render(request, 'galeria/imagem.html')
