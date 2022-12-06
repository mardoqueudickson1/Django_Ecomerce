from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views import View
from . import models


from . import models
from . import forms


class BasePerfil(View):
    template_name = 'perfil/login.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:

            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user,
                ),

                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }
        else:
            self.contexto = {
                'userform': forms.UserForm(
                    data=self.request.POST or None
                ),

                'perfilform': forms.PerfilForm(
                    data=self.request.POST or None
                )
            }




        self.renderizar = render(
            self.request, self.template_name, self.contexto
        )

    def get(self, *args, **kwargs):
        return self.renderizar




class Criar(BasePerfil):
    def post(self, *args, **kwargs):
        return self.renderizar


class Atualizar(View):
    def get(self, *args,**kwargs):
        return HttpResponse('Atualizar')


class Login(ListView):
    model = models.Perfil
    template_name = 'perfil/login.html'


class Cadastro(ListView):
    model = models.Perfil
    template_name = 'perfil/cadastro.html'

class Logout(View):
    def get(self, *args,**kwargs):
        return HttpResponse('Logout')
