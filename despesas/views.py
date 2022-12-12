from django.shortcuts import render, get_object_or_404, redirect
from .models import Despesas
from .forms import *
# Create your views here.

def index(request):
    return render(request, 'receita/index.html')

def listDespesas(request):
    despesas = Despesas.objects.all()
    return render(request, 'despesas/listDespesas.html', {'despesas': despesas})

def receitaView(request, id):
    despesa = get_object_or_404(Despesas, pk=id)
    return render(request, 'despesas/despesa.html', {'despesa': despesa})

def newdespesa(request):
    if request.method == 'POST':
        form = despesaForm(request.POST)
        
        if form.is_valid():
            despesa = form.save()
            return redirect('/despesas/listDespesas')
    else:     
        form = despesaForm()
        return render(request, 'despesas/adddespesa.html', {'form': form})
    
def editdespesa(request, id):
    despesa = Despesas.objects.get(pk = id)
    form = despesaForm(instance=despesa)
    
    if request.method == 'GET':
        return render(request, 'despesas/editdespesa.html', {'form': form})
    else:
        form = despesaForm(request.POST, instance = despesa)
        if form.is_valid():
            form.save()
            return redirect('/despesas/listDespesas')
        else:
            form = despesaForm()
            return render(request,'despesas/editdespesa.html', {'form':form})
        
def deletedespesa(request, id):
    despesa = Despesas.objects.get(pk = id)
    despesa.delete()
    return redirect('/despesas/listDespesas')