from django.db import models

class Pessoa(models.Model):
	nome = models.CharField('Nome', max_length=200)
	email = models.CharField('Email', max_length=200)

	def __str__(self):
		return self.nome