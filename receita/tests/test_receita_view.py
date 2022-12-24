from django.test import TestCase
from django.urls import reverse
from receita.models import Categoria, Receitas

class Tests_Views(TestCase):
    def test_index(self):
        response = self.client.get(reverse("index"))
        assert response.status_code == 200

    def test_receita_List(self):
        response = self.client.get(reverse("listReceita"))
        assert response.status_code == 200

    def test_new_receita(self):  
        response = self.client.post(reverse("author-add"))
        assert response.status_code == 200
        
    def test_edit_receita(self):
        categoria = Categoria.objects.create(nome = 'salario')
        categoria.save()
        receita = Receitas.objects.create(pk = 1, nome = 'Salario', valor = 1500, categoria = categoria)
        receita.save()
        
        response = self.client.post(reverse('editReceita', kwargs={'pk':1}),
                                    {
                                        'nome' : 'Salarioo',
                                        'valor' : 1600,
                                        'categoria' : 'salario',
                                    }, follow=True)
        assert response.status_code == 200
        
    def test_delete_receita(self):
        categoria = Categoria.objects.create(nome = 'salario')
        categoria.save()
        receita = Receitas.objects.create(id = 1, nome = 'Salario', valor = 1500, categoria = categoria)
        receita.save()
        
        response = self.client.get(reverse('delete-receita' , kwargs={'id':1}), follow=True)
        assert response.status_code == 200
        
