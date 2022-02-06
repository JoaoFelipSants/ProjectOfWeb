from django.urls import path
from .views import PerfilCreate,  CategoriaCreate,  NoticiaCreate
from .views import PerfilUpdate, CategoriaUpdate, NoticiaUpdate
from .views import PerfilList, CategoriaList, NoticiaList
urlpatterns = [
    #todas as rotas vao ser assim
    #path('inicio/', PaginaInicial.as_view(),name='index'),

    path('cadastrar/perfil/', PerfilCreate.as_view(), name='cadastrar-perfil'),
    path('editar/perfil/<int:pk>/', PerfilUpdate.as_view(), name='editar-perfil'),
    path('listar/perfil/', PerfilList.as_view(), name='listar-perfil'),

    path('cadastrar/categoria/', CategoriaCreate.as_view(), name='cadastrar-categoria'),
    path('editar/categoria/<int:pk>/', CategoriaUpdate.as_view(), name='editar-categoria'),
    path('listar/categoria/', CategoriaList.as_view(), name='listar-categoria'),

    path('cadastrar/noticia/', NoticiaCreate.as_view(), name='cadastrar-noticia'),
    path('editar/noticia/<int:pk>/', NoticiaUpdate.as_view(), name='editar-noticia'),
    path('listar/noticia/', NoticiaList.as_view(), name='listar-noticia'),
]