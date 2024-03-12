from django.db import models
from datetime import date

class PessoaFemininoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genero = 'f')

class PessoaMasculinoManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(genero = 'm')
    
class PessoaManager(models.Manager):
    def masculino(self):
        return self.filter(genero = 'm')
    
    def feminino(self):
        return self.filter(genero = 'f')
    


class Pessoa(models.Model):
    nome = models.CharField(max_length=100)
    genero = models.CharField(max_length=1)
    nascimento = models.DateField()
    
    objects = PessoaManager()

    # masculino = PessoaMasculinoManager()
    # feminino = PessoaFemininoManager()
    # objects = PessoaManager()
    
    
    def __str__(self) -> str:
        return self.nome

    @property
    def idade(self):
        today = date.today()
        return today.year - self.nascimento.year - ((today.month, today.day) < (self.nascimento.month, self.nascimento.day))

    

   