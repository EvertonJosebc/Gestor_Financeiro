from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_url_index(self):
        url = reverse('index')
        self.assertEquals(url, '/')
        
    def test_url_list_receita(self):
        url = reverse('listReceita')
        self.assertEquals(url, '/listReceita/')
        
    def test_url_new_receita(self):
        url = reverse('author-add')
        self.assertEquals(url, '/newReceita/')
        
    def test_url_edit_receita(self):
        url = reverse('editReceita', kwargs={'pk' : 1})
        self.assertEquals(url, '/editReceita/1')
        
    def test_url_delete_receita(self):
        url = reverse('delete-receita', kwargs={'id' : 1})
        self.assertEquals(url, '/deleteReceita/1')
        
    def test_url_receita_id(self):
        url = reverse('receita-View', kwargs={'id': 1})
        self.assertEquals(url, '/receita/1')