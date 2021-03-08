from django.shortcuts import render


def home(request):
    return render(request, 'base/home.html')


def consultar(request):
    return render(request, 'base/consultar.html')


def cadastrar(request):
    return render(request, 'base/cadastrar.html')


def alterar(request):
    return render(request, 'base/alterar.html')
