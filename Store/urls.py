

from unicodedata import name
from django.urls import path
from Store import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('teste', views.teste, name='teste'),
    path('departamentos',views.departamentos, name='departamentos'),# CAMINHO PARA A VIWS
    path('categoria/<int:id>',views.categoria, name= 'categoria'),
    path('produtos/<int:id>',views.produto,name='produto')
]