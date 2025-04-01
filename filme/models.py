from django.db import models

# Create your models here.
class Generos(models.Model):
    genero = models.CharField('Genero', max_length=100)

    def __str__(self):
        return self.genero
    
    class Meta:
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        ordering = ['genero']

class Filmes(models.Model):
    filme = models.CharField('Nome', max_length=100)
    genero = models.ForeignKey(Generos, on_delete=models.PROTECT)
    quantidade = models.IntegerField('Quantidade', default=0)
    preco = models.FloatField('Preço', max_length=8)

    def __str__(self):
        return self.filme

    class Meta:
        verbose_name = 'Filme'
        verbose_name_plural = 'Filmes'
        ordering = ['filme']
    
