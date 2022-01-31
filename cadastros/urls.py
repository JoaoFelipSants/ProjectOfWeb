from django.urls import path
from .views import PerfilCreate, PerfilUpdate, CategoriaCreate, CategoriaUpdate, NoticiaCreate, NoticiaUpdate

urlpatterns = [
    #todas as rotas vao ser assim
    #path('inicio/', PaginaInicial.as_view(),name='index'),

    path('cadastrar/perfil/', PerfilCreate.as_view(), name='cadastrar_perfil'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar_perfil'),

    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar_categoria'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar_categoria'),

    path('cadastrar/noticia/', NoticiaCreate.as_view(), name='cadastrar_noticia'),
    path('editar/noticia/<int:pk>/', NoticiaUpdate.as_view(), name='editar_noticia'),

]