from django.db import models

# Create your models here.
class Pessoas(models.Model):
    nome = models.CharField('Nome', max_length=200)
    telefone = models.CharField('Telefone', max_length=11)
    idade = models.IntegerField('Idade', null=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        verbose_name = 'Pessoa'
        verbose_name_plural = 'Pessoas'
        ordering = ['nome']