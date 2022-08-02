from http.client import HTTPResponse
from math import prod
from multiprocessing import context
from django.shortcuts import render
from Store.models import Departamento, Categoria, Produto


# Create your views here.
def index(request):
    meu_nome = "Jefferson Gonçalves Dos Santos"
    sexo = "a"
    context = {'nome': meu_nome, "artigo": "o" if sexo=="m" else "a"}
    return render(request,'index.html',context)

# def teste(request):
#     # depto = ['Casa','Informatica','Telefonia','Gamer']
#     depto = Departamento.objects.all()
#     context = {'departamentos':depto}
#     return render(request,'teste.html',context)

# FUNCOES QUE CHAMA MOLDELS E ENVIA PARA HTML
def departamentos(request):
    depto = Departamento.objects.all()
    context = {'departamentos':depto}
    return render(request,'departamentos.html',context)  


def categoria(request, id):
    cat = Categoria.objects.filter(departamento_id = id)
    context = {'categoria':cat}
    return render(request,'categoria.html',context)   

def produto(request,id):
    prod = Produto.objects.filter(categoria_id = id)
    context = {'produtos':prod}
    return render(request,'produtos.html',context)       



