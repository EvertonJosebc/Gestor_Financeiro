from django.test import TestCase
from django.urls import reverse
from django.test.client import Client

class TestUrls(TestCase):
    def setUp(self):
        self.client = Client()
        
    def test_url_list_despesa(self):
        url = reverse('list-Despesas')
        self.assertEquals(url, '/despesas/listDespesas/')
        
    def test_url_new_despesa(self):
        url = reverse('new-despesa')
        self.assertEquals(url, '/despesas/adddespesa/')
        
    def test_url_edit_despesa(self):
        url = reverse('edit-despesa', kwargs={'id' : 1})
        self.assertEquals(url, '/despesas/editdespesa/1')
        
    def test_url_delete_despesa(self):
        url = reverse('delete-despesa', kwargs={'id' : 1})
        self.assertEquals(url, '/despesas/deletedespesa/1')