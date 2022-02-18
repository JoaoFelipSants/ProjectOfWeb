from nntplib import GroupInfo
from django.contrib.auth.mixins import LoginRequiredMixin
from braces.views import GroupRequiredMixin
from pyexpat import model
from tkinter.ttk import Button
from .models import Perfil, Categoria, Noticia, Visualizacao, Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


class PerfilCreate(CreateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'cpf', 'data_nasc', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('inicio') # Redireciona o usuário para "index"
           

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'bio', 'senha']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-perfil') # Redireciona o usuário para "index"

    
class PerfilList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class PerfilDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-perfil')


class CategoriaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

class CategoriaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

    
class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'


class CategoriaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"admin"
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-categoria')

class NoticiaCreate(LoginRequiredMixin, GroupRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    group_required = u"escritor"
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"

class NoticiaUpdate(LoginRequiredMixin, GroupRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    group_required = u"escritor"
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"


class NoticiaList(ListView):
    login_url = reverse_lazy('login')
    model = Noticia
    template_name = 'cadastros/listas/noticia.html'

    
class NoticiaDelete(LoginRequiredMixin, GroupRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    group_required = u"escritor", u"admin"
    model = Noticia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-noticia')