

from pyexpat import model
from tkinter.ttk import Button
from .models import Perfil, Categoria, Noticia, Visualizacao, Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome','cpf', 'data_nasc', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-perfil') # Redireciona o usuário para "index"
           


class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-perfil') # Redireciona o usuário para "index"

    
class PerfilList(ListView):
    model = Perfil
    template_name = 'cadastros/listas/perfil.html'

class PerfilDelete(DeleteView):
    model = Perfil
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-perfil')


class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-categoria') # Redireciona o usuário para "index"

    
class CategoriaList(ListView):
    model = Categoria
    template_name = 'cadastros/listas/categoria.html'


class CategoriaDelete(DeleteView):
    model = Categoria
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-categoria')

class NoticiaCreate(CreateView):
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"

class NoticiaUpdate(UpdateView):
    model = Noticia
    fields = ['titulo', 'tags', 'conteudo', 'vizualizacao', 'categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('listar-noticia') # Redireciona o usuário para "index"


class NoticiaList(ListView):
    model = Noticia
    template_name = 'cadastros/listas/noticia.html'

    
class NoticiaDelete(DeleteView):
    model = Noticia
    template_name = 'cadastros/form-excluir.html'
    success_url = reverse_lazy ('listar-noticia')