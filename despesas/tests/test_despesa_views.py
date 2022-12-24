from django.test import TestCase
from django.urls import reverse
from despesas.models import Categoria, Despesas

class Tests_Views(TestCase):

    def test_despesa_List(self):
        response = self.client.get(reverse("list-Despesas"))
        assert response.status_code == 200

    def test_new_despesa(self):  
        response = self.client.post(reverse('new-despesa'))
        assert response.status_code == 200
        
    def test_edit_despesa(self):
        categoria = Categoria.objects.create(nome = 'salario')
        categoria.save()
        despesa = Despesas.objects.create(id = 1, nome = 'Salario', valor = 1500, categoria = categoria)
        despesa.save()
        
        response = self.client.post(reverse('edit-despesa', kwargs={'id':1}),
                                    {
                                        'nome' : 'Salarioo',
                                        'valor' : 1600,
                                        'categoria' : 'salario',
                                    }, follow=True)
        assert response.status_code == 200
        
    def test_delete_despesa(self):
        categoria = Categoria.objects.create(nome = 'salario')
        categoria.save()
        despesa = Despesas.objects.create(id = 1, nome = 'Salario', valor = 1500, categoria = categoria)
        despesa.save()
        
        response = self.client.get(reverse('delete-despesa' , kwargs={'id':1}), follow=True)
        assert response.status_code == 200