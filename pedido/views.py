import imp
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View


class Pagar(View):
    def get(self, *args, **kwargs):
        return HttpResponse('PAGAR')


class FecharPedido(View):
    def get(*args, **kwargs):
        return HttpResponse('FECHAR PEDIDO')



class Detalhes(View):
    def get(*args, **kwargs):
        return HttpResponse('FECHAR PEDIDO')