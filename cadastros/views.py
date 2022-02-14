from django.contrib.auth.mixins import LoginRequiredMixin
from pyexpat import model
from tkinter.ttk import Button
from .models import Perfil, Categoria, Noticia, Visualizacao, Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy


class PerfilCreate( LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome','cpf', 'data_nasc', 'bio', 'usuario']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-perfil') # Redireciona o usuário para "index"
           

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Perfil
    fields = ['nome', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-perfil') # Redireciona o usuário para "index"

    
class PerfilList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class PerfilDelete(DeleteView):
    login_url = reverse_lazy('login')
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-perfil')


class CategoriaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

class CategoriaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

    
class CategoriaList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'


class CategoriaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-categoria')

class NoticiaCreate(LoginRequiredMixin, CreateView):
    login_url = reverse_lazy('login')
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"

class NoticiaUpdate(LoginRequiredMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"


class NoticiaList(ListView):
    login_url = reverse_lazy('login')
    model = Noticia
    template_name = 'cadastros/listas/noticia.html'

    
class NoticiaDelete(LoginRequiredMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Noticia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-noticia')