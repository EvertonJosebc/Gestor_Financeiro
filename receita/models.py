from django.db import models
from django.urls import reverse
    
class Categoria(models.Model):
    nome = models.CharField(max_length= 150)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('categoria-detail', kwargs={'pk': self.pk})
    
class Receitas(models.Model):
    nome = models.CharField(max_length=150)
    valor = models.FloatField()
    categoria = models.ForeignKey(Categoria, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.nome
    
    def get_absolute_url(self):
        return reverse('receitas-detail', kwargs={'pk': self.pk})
    
    def get_delete_url(self):
        return reverse('delete-receita', kwargs={'pk': self.pk})

    