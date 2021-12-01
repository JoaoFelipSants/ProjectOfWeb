from django.urls import path
from .views import PaginaInicial

urlpatterns = [
    #todas as rotas vao ser assim
    path('inicio/', PaginaInicial.as_view(),name='index'),

]