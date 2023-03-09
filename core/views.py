from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin


class IndexView(LoginRequiredMixin, TemplateView):
    """
    Esse primeiro atributo da classe 'LoginRequiredMixin', não permite que o usuário acesse ao template sem estar logado
    o deixando em um loop infinito até ele logar
    """
    template_name = 'index.html'


class LoginView(TemplateView):
    """
    Essa é a página de login
    """
    template_name = 'login.html'
