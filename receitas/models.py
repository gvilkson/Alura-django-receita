from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


# Create your models here.
class Receita(models.Model):
	pessoa = models.ForeignKey(User, on_delete=models.CASCADE)
	nome_receita = models.CharField('Nome da receita', max_length=200)
	ingredientes = models.TextField('Ingredientes')
	modo_preparo = models.TextField('Modo de preparo')
	tempo_preparo = models.IntegerField('Tempo de preparo')
	rendimento = models.TextField('Rendimento', max_length=100)
	categoria = models.CharField('Categoria', max_length=100)
	date_receita = models.DateTimeField(default=datetime.now, blank=True)
	foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)
	publicada = models.BooleanField(default=False)

	def __str__(self):
		return self.nome_receita