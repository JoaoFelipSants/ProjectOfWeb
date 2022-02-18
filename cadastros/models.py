from email.policy import default
from django.db import models
from django.contrib.auth.models import User

class Perfil (models.Model):
    nome = models.CharField(max_length=50, null=False)
    # senha = models.CharField(min_lenght=6, max_lenght=25, null=False)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField()
    bio = models.TextField()
    #usuario = models.OneToOneField(User, on_delete=models.PROTECT)

    #foto_perfil = models.ImageField()
    def __str__(self):
        return "{} - {} - {}".format(self.nome, self.cpf, self.bio) #tem que criar esse def para todas as classes man deixei pausado na video aula do prof explicando como faz eu sinceramente nn me lembro para o que serve


class Categoria (models.Model):
    nome =  models.CharField(max_length=50)

    def __str__(self):
        return "{}".format(self.nome)


class Noticia (models.Model):
    titulo = models.CharField(max_length=30)
    tags = models.CharField(max_length=50)
    data_publi = models.DateTimeField(auto_now_add=True) # DateField possivelmente dando erro.
    conteudo = models.TextField()
    vizualizacao = models.IntegerField(default=0)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return "{} - {} - {} - {}".format(self.titulo, self.categoria, self.conteudo, self.tags)


class Comentario (models.Model):
    conteudo = models.CharField(max_length=255)
    comentado_em = models.DateTimeField(auto_now_add=True)
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    def __str__(self):
        return "{} - {} - {}".format(self.conteudo, self.comentado_em, self.noticia.titulo)

######  Não vai usar ######

class Visualizacao (models.Model):
    visualizado_em = models.DateTimeField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)

    def __str__(self):
        return '{} - {}'.format(self.visualizado_em, self.noticia.titulo)
