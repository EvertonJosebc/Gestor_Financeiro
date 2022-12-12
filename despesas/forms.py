from django import forms
from .models import Despesas, Categoria

class despesaForm(forms.ModelForm):
    
    class Meta:
        model = Despesas
        fields = '__all__'
        
class categoriaForm(forms.ModelForm):
    
    class Meta:
        model = Categoria
        fields = '__all__'