from django.urls import path
from .views import *

despesas = 'app_despesas'

urlpatterns = [
    path('listDespesas/', listDespesas, name="list-Despesas"),
    path('adddespesa/', newdespesa, name="new-despesa"),
    path('editdespesa/<int:id>', editdespesa, name="edit-despesa"),
    path('deletedespesa/<int:id>', deletedespesa, name="delete-despesa")
]