from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Receitas, Categoria
from despesas.models import Despesas
from .forms import *
# Create your views here.

def index(request):
    receitas = Receitas.objects.all()
    soma_receita = 0
    for i in receitas:
        soma_receita += i.valor
        
    despesas = Despesas.objects.all()
    soma_despesa = 0
    for i in despesas:
        soma_despesa += i.valor
        
    saldo = soma_receita - soma_despesa
    
    labels = []
    data = []

    queryset = Receitas.objects.order_by('-valor')[:5]
    for i in queryset:
        labels.append(i.nome)
        data.append(i.valor)
    
    return render(request, 'receita/index.html', {'soma' : soma_receita,
                                                  'diminuir' : soma_despesa,
                                                  'saldo' : saldo,
                                                  'labels': labels,
                                                  'data': data,})
    

def receitaList(request):
    receitas = Receitas.objects.all()
    return render(request, 'receita/receita.html', {'receitas': receitas})

def receitaView(request, id):
    receita = get_object_or_404(Receitas, pk=id)
    return render(request, 'receita/receita.html', {'receita': receita})

def newReceita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        
        if form.is_valid():
            receita = form.save()
            return redirect('/listReceita')
    else:     
        form = ReceitaForm()
        return render(request, 'receita/addreceita.html', {'form': form})
    
def editReceita(request, id):
    receita = Receitas.objects.get(pk = id)
    form = ReceitaForm(instance=receita)
    
    if request.method == 'GET':
        return render(request, 'receita/editReceita.html', {'form': form})
    else:
        form = ReceitaForm(request.POST, instance = receita)
        if form.is_valid():
            form.save()
            return redirect('/listReceita')
        else:
            form = ReceitaForm()
            return render(request,'receita/editReceita.html', {'form':form})
        
def deleteReceita(request, id):
    receita = Receitas.objects.get(pk = id)
    receita.delete()
    return redirect('/listReceita')

def newCategoria(request):
    if request.method == 'POST':
        form = categoriaForm(request.POST)
        
        if form.is_valid():
            receita = form.save()
            return redirect('/listReceita')
    else:
        categoria = request.POST["nome"]

        Categoria.objects.create(nome = categoria)
        return redirect('index.html')
