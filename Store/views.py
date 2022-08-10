from distutils.errors import DistutilsTemplateError
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
    depto = Departamento.objects.get(id=id)
    context = {'categoria':cat,
               'departamento':depto 
                }
    return render(request,'categoria.html',context)   

    

def produto(request,id):
    prod = Produto.objects.filter(categoria_id = id)
    categ = Categoria.objects.get(id=id)
    context = {'produtos':prod,
                'categoria': categ
                }
    return render(request,'produtos.html',context)  


def produto_detalhe(request,id):# linha que faz uma requisicao
    prode = Produto.objects.get(id = id) # linha qua pega arquivo no model/ banco de daos
    context = {'produto':prode} # linha que chama json na pagina html
    return render (request,'produto_detalhe.html',context)# linha que chama pagina html

def institucional (request):
    return render(request,'institucional.html')

def contato (request):
    return render(request,'contato.html')   