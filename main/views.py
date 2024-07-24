import os
from django.shortcuts import render, redirect
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from .models import Motorista, Container, Carga, Desunitição_e_Unitização, Preenchimento, Cedido
from .forms import Desunitição_e_UnitizaçãoForm, MotoristaForm, ContainerForm, CargaForm, Preenchimento, CedidoForm
from datetime import datetime, timedelta
from django.db.models import Count

import tempfile

# Create your views here.
@login_required
def Home(request):

    # Consultar o tipo de preenchimento 'Cheio' e 'Vazio'
    preenchimento_cheio = Preenchimento.objects.get(tipo='Cheio')
    preenchimento_vazio = Preenchimento.objects.get(tipo='Vazio')

    # Contagem de containers cheios e vazios
    containers_cheios = Container.objects.filter(preenchimento=preenchimento_cheio).count()
    containers_vazios = Container.objects.filter(preenchimento=preenchimento_vazio).count()
    
    # Calcular entradas e saídas no mês atual
    data_atual = datetime.now().date()
    mes_atual = data_atual.month
    ano_atual = data_atual.year

    entradas_mes = Container.objects.filter(data_entrada__month=mes_atual, data_entrada__year=ano_atual).count()
    saidas_mes = Container.objects.filter(data_saida__month=mes_atual, data_saida__year=ano_atual).count()

    # Contagem de desunitizações
    desunitizacoes_count = Desunitição_e_Unitização.get_desunitizacoes_count()

    # Consultar as entradas e saídas diárias de containers para o gráfico
    first_day = datetime(ano_atual, mes_atual, 1)
    if mes_atual == 12:
        last_day = datetime(ano_atual + 1, 1, 1) - timedelta(days=1)
    else:
        last_day = datetime(ano_atual, mes_atual + 1, 1) - timedelta(days=1)

    entries = Container.objects.filter(data_entrada__date__range=[first_day, last_day]).values('data_entrada__date').annotate(count=Count('id'))
    exits = Container.objects.filter(data_saida__date__range=[first_day, last_day]).values('data_saida__date').annotate(count=Count('id'))

    data = {}
    for entry in entries:
        data[entry['data_entrada__date']] = {'entries': entry['count'], 'exits': 0}
    for exit in exits:
        if exit['data_saida__date'] in data:
            data[exit['data_saida__date']]['exits'] = exit['count']
        else:
            data[exit['data_saida__date']] = {'entries': 0, 'exits': exit['count']}

    labels = []
    entries_data = []
    exits_data = []
    current_date = first_day
    while current_date <= last_day:
        labels.append(current_date.strftime('%Y-%m-%d'))
        if current_date in data:
            entries_data.append(data[current_date]['entries'])
            exits_data.append(data[current_date]['exits'])
        else:
            entries_data.append(0)
            exits_data.append(0)
        current_date += timedelta(days=1)



    context = {
        'containers_cheios': containers_cheios,
        'containers_vazios': containers_vazios,
        'entradas_mes': entradas_mes,
        'saidas_mes': saidas_mes,
        'labels': labels,
        'entries_data': entries_data,
        'exits_data': exits_data,
        'desunitizacoes_count': desunitizacoes_count,
    }

    return render(request, 'main/index.html', context)


@login_required
def relatorio(request):
    container = Container.objects.all()
    form = ContainerForm()
    data = {'container': container, 'form': form}
    return render(request, 'main/relatorio.html', data)

#---------- definições de urls

@login_required
def cadastro_motorista(request):
    motorista = Motorista.objects.all()
    form = MotoristaForm()
    data = {'motorista': motorista, 'form': form}
    return render(request,'main/cadastro_motorista.html', data)


@login_required
def cadastro_desunitizacao(request):
    desunitizacao = Desunitição_e_Unitização.objects.all()
    form = Desunitição_e_UnitizaçãoForm()
    data = {'desunitizacao': desunitizacao, 'form': form}
    return render(request,'main/cadastro_desunitizacao.html', data)


@login_required
def cadastro_container(request):
    container = Container.objects.all()
    form = ContainerForm()
    data = {'container': container, 'form': form}
    return render(request,'main/cadastro_container.html', data)


@login_required
def cadastro_carga(request):
    carga = Carga.objects.all()
    form = CargaForm()
    data = {'carga': carga, 'form': form}
    return render(request,'main/cadastro_carga.html', data)


@login_required
def cadastro_cedido(request):
    cedido = Cedido.objects.all()
    form = CedidoForm()
    data = {'cedido': cedido, 'form': form}
    return render(request, 'main/cadastro_cedido.html', data)

#========== ETAPA CRUD ==========

#========== CREATE ==========

@login_required
def motorista_novo(request):
    if request.method == 'POST':
        form = MotoristaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_lista_motorista')
    else:
        form = MotoristaForm()

    data = {'form': form}
    return render(request, 'main/cadastro_motorista.html', data)


@login_required
def desunitizacao_novo(request):
    if request.method == 'POST':
        form = Desunitição_e_UnitizaçãoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_lista_desunitizacao')
    else:
        form = Desunitição_e_UnitizaçãoForm()

    data = {'form': form}
    return render(request, 'main/cadastro_desunitizacao.html', data)


@login_required
def carga_novo(request):
    if request.method == 'POST':
        form = CargaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_lista_carga')
    else:
        form = CargaForm()

    data = {'form': form}
    return render(request, 'main/cadastro_carga.html', data)


@login_required
def container_novo(request):
    if request.method == 'POST':
        form = ContainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_lista_container')
    else:
        form = ContainerForm()

    data = {'form': form}
    return render(request, 'main/cadastro_container.html', data)


@login_required
def cedido_novo(request):
    if request.method == 'POST':
        form = CedidoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('main_lista_cedido')
    else:
        form = CedidoForm()

    data = {'form': form}
    return render(request, 'main/cadastro_cedido.html', data)

#========== Read ==========

@login_required
def lista_carga(request):
    carga = Carga.objects.all()
    form = CargaForm()
    data = {'carga': carga, 'form': form}
    return render(request,'main/lista_carga.html', data)


@login_required
def lista_container(request):
    container = Container.objects.all()
    form = ContainerForm()
    data = {'container': container, 'form': form}
    return render(request, 'main/lista_container.html', data)


@login_required
def lista_desunitizacao(request):
    desunitizacao = Desunitição_e_Unitização.objects.all()
    form = Desunitição_e_UnitizaçãoForm()
    data = {'desunitizacao': desunitizacao, 'form': form}
    return render(request, 'main/lista_desunitizacao.html', data)


@login_required
def lista_motorista(request):
    motorista = Motorista.objects.all()
    form = MotoristaForm()
    data = {'motorista': motorista, 'form': form}
    return render(request, 'main/lista_motorista.html', data)


@login_required
def lista_cedido(request):
    cedido = Cedido.objects.all()
    form = CedidoForm()
    data = {'cedido': cedido, 'form': form}
    return render(request, 'main/lista_cedido.html', data)


#========== Update ==========


@login_required
def desunitizacao_update(request, id):
    data = {}
    transportadora = Desunitição_e_Unitização.objects.get(id=id)
    form = Desunitição_e_UnitizaçãoForm(request.POST or None, instance=transportadora)
    data['transportadora'] = transportadora
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_lista_desunitizacao')
    else:
        return render(request, 'main/update_desunitizacao.html', data)
    

@login_required
def motorista_update(request, id):
    data = {}
    motorista = Motorista.objects.get(id=id)
    form = MotoristaForm(request.POST or None, instance=motorista)
    data['motorista'] = motorista
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_lista_motorista')
    else:
        return render(request, 'main/update_motorista.html', data)
    


@login_required
def container_update(request, id):
    data = {}
    container = Container.objects.get(id=id)
    form = ContainerForm(request.POST or None, instance=container)
    data['container'] = container
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_lista_container')
    else:
        return render(request, 'main/update_container.html', data)
    

@login_required
def carga_update(request, id):
    data = {}
    carga = Carga.objects.get(id=id)
    form = CargaForm(request.POST or None, instance=carga)
    data['carga'] = carga
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_lista_carga')
    else:
        return render(request, 'main/update_carga.html', data)
    

@login_required
def cedido_update(request, id):
    data = {}
    cedido = Cedido.objects.get(id=id)
    form = CedidoForm(request.POST or None, instance=cedido)
    data['cedido'] = cedido
    data['form'] = form

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('main_lista_cedido')
    else:
        return render(request, 'main/update_cedido.html', data)