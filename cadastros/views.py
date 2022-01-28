from django.shortcuts import render
from django.db.models import fields
from django.urls.base import reverse
from .models import Perfil, Categoria, Noticia, Visualizacao, Comentario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

class PerfilCreate(CreateView):
    model = Perfil
    fields = ['nome','cpf', 'data_nasc', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"

class PerfilUpdate(UpdateView):
    model = Perfil
    fields = ['nome','cpf', 'data_nasc', 'bio']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"

class CategoriaCreate(CreateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"

class CategoriaUpdate(UpdateView):
    model = Categoria
    fields = ['nome']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"

class NoticiaCreate(CreateView):
    model = Noticia
    fields = ['titulo, tags, conteudo, visualizacao, categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"

class NoticiaUpdate(UpdateView):
    model = Noticia
    fields = ['titulo, tags, conteudo, visualizacao, categoria']
    template_name = 'cadastros/form.html'
    success_url = reverse_lazy ('index') # Redireciona o usuário para "index"
