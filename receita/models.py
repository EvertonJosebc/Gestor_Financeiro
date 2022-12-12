from django.db import models
    
class Categoria(models.Model):
    nome = models.CharField(max_length= 150)
    
    def __str__(self):
        return self.nome
    
class Receitas(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nome

    