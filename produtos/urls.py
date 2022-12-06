from pathlib import Path
from unicodedata import name
from django.urls import path
from . import views

upp_name = 'produto'

urlpatterns = [
    path('', views.ListaProduto.as_view(), name='lista'),
    path('produtos/', views.Produtos.as_view(), name='produtos'),
    path('<slug>', views.DetalheProduto.as_view(), name='detalhe'),
    path('adicionaraocarrinho/', views.AdicionarAoCarrinho.as_view(), name='adicionaraocarrinho'),
    path('removerdocarrinho/', views.RemoverDoCarrinho.as_view(), name='removerdocarrinho'),
    path('carrinho/', views.Carrinho.as_view(), name='Carrinho'),

    

] 

