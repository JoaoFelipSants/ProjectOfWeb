from django.db import models

class Perfil (models.Model):
    nome = models.CharField(max_length=50)
    cpf = models.CharField(max_length=14)
    data_nasc = models.DateField() # DateField possivelmente dando erro.
    bio = models.CharField(max_length=60)
    #foto_perfil = models.ImageField()
    def __str__(self):
        return '{} - {} - {}'.format(self.nome, self.cpf, self.bio) #tem que criar esse def para todas as classes man deixei pausado na video aula do prof explicando como faz eu sinceramente nn me lembro para o que serve

class Categoria (models.Model):
    nome =  models.CharField(max_length=50)
    def __str__(self):
        return '{}'.format(self.nome)

class Noticia (models.Model):
    titulo = models.CharField(max_length=30)
    tags = models.CharField(max_length=15)
    data_publi = models.DateTimeField() # DateField possivelmente dando erro.
    conteudo = models.TextField()
    vizualizacao = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    def __str__(self):
        return '{} - {} - {} - {} - {}'.format(self.titulo, self.tags, self.conteudo, self.vizualizacao, self.categoria.nome)

class Visualizacao (models.Model):
    visualizado_em = models.DateTimeField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    def __str__(self):
        return '{} - {}'.format(self.visualizado_em, self.noticia.titulo)

class Comentario (models.Model):
    conteudo = models.CharField(max_length= 120)
    comentado_em = models.DateTimeField()
    noticia = models.ForeignKey(Noticia, on_delete=models.CASCADE)
    def __str__(self):
        return '{} - {} - {}'.format(self.conteudo, self.comentado_em, self.noticia.titulo)
