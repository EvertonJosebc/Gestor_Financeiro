from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.index, name="index"),
    path('receita/<int:id>', views.receitaView, name='receita-View'),
    path('listReceita/', ListReceita.as_view(), name = 'listReceita'),
    path('newReceita/', newReceita.as_view(), name='author-add'),
    path('editReceita/<int:pk>', editReceita.as_view(), name="editReceita"),
    path('deleteReceita/<int:id>', views.deleteReceita, name="delete-receita")
]
