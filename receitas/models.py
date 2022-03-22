from django.db import models
from datetime import datetime


# Create your models here.
class Receita(models.Model):
	nome_receita = models.CharField('Nome da receita', max_length=200)
	ingredientes = models.TextField('Ingredientes')
	modo_preparo = models.TextField('Modo de preparo')
	tempo_preparo = models.IntegerField('Tempo de preparo')
	rendimento = models.TextField('Rendimento', max_length=100)
	categoria = models.CharField('Categoria', max_length=100)
	date_receita = models.DateTimeField(default=datetime.now, blank=True)

	def __str__(self):
		return self.nome_receita