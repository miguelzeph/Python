from django.db import models

# Create your models here.

class Arquivo(models.Model):

    nome = models.CharField(max_length=15)
    texto = models.TextField()

    def __str__(self):
       return 'Arquivo' + '_'+ self.nome

