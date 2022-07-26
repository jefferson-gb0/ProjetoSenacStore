from http.client import HTTPResponse
from multiprocessing import context
from django.shortcuts import render
from Store.models import Departamento

# Create your views here.
def index(request):
    meu_nome = "Jefferson Gonçalves Dos Santos"
    sexo = "a"
    context = {'nome': meu_nome, "artigo": "o" if sexo=="m" else "a"}
    return render(request,'index.html',context)

def teste(request):
    # depto = ['Casa','Informatica','Telefonia','Gamer']
    depto = Departamento.objects.all()
    context = {'departamentos':depto}
    return render(request,'teste.html',context)