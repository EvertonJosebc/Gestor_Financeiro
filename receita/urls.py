from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('receita/<int:id>', views.receitaView, name='receita-View'),
    path('listReceita/', views.receitaList, name="receita-List"),
    path('newReceita/', views.newReceita, name="new-Receita"),
    path('editReceita/<int:id>', views.editReceita, name="edit-Receita"),
    path('deleteReceita/<int:id>', views.deleteReceita, name="delete-Receita")
]
