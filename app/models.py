from django.db import models

class Musicas(models.Model):
	nome = models.CharField('Nome', max_length = 100)
	autor = models.CharField('Autor', max_length=100)
	link = models.CharField('Link', max_length = 300)
	
	def __str__(self):
		return self.nome
