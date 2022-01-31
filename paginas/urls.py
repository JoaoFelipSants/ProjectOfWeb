from django.urls import path
from .views import PaginaInicial, Sobre

urlpatterns = [
    #todas as rotas vao ser assim
    path('inicio/', PaginaInicial.as_view(),name='index'),
    path('', PaginaInicial.as_view(), name='index-2'),
    
    path('sobre/', Sobre.as_view(), name='sobre'),
]