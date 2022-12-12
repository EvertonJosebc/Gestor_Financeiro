from django import forms
from .models import Receitas, Categoria

class ReceitaForm(forms.ModelForm):
    
    class Meta:
        model = Receitas
        fields = '__all__'
        
class categoriaForm(forms.ModelForm):

    class Meta:
        model = Categoria
        fields = '__all__'