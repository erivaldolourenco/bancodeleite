import datetime

from django.contrib.auth import logout as dash_logout, authenticate, login as dash_login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages

from bdleite.forms import DoadoraForm, EnderecoForm, ContatoForm
from bdleite.models import Doadora, Endereco, Contato, Funcionario


# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST['inputUser']
        password = request.POST['inputPassword']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            dash_login(request, user)
            messages.add_message(
                request, messages.SUCCESS, 'Bem-vindo ' +
                str(user.first_name)+' '+str(user.last_name)+'!',
                fail_silently=True,
            )
            return redirect('/')
        else:
            messages.add_message(
                request, messages.ERROR, 'Usuário ou senha inválidos :(',
                fail_silently=True,
            )
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')

@login_required
def logout(request):
    dash_logout(request)
    return redirect('/login')

@login_required
def home(request):
    template = loader.get_template('home.html')
    context = {
        'user': dir(request.user.funcionario_set),
    }
    return HttpResponse(template.render(context, request))

@login_required
def doadoras(request):
    template = loader.get_template('bdleite/doadoras.html')

    doadoras = Doadora.objects.all()
    context = {
        'doadoras': doadoras,
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_doadora(request):
    if request.method == 'POST':
        doadora = Doadora()
        endereco = Endereco()
        contato = Contato()
        form_doadora = DoadoraForm(request.POST, request.FILES, instance=doadora)
        form_endereco = EnderecoForm(request.POST, request.FILES, instance=endereco)
        form_contato = ContatoForm(request.POST, request.FILES, instance=contato)
        if form_doadora.is_valid() and form_endereco.is_valid() and form_contato.is_valid():
            doadora = form_doadora.save(commit=True)
            doadora.endereco = form_endereco.save(commit=True)
            doadora.contato = form_contato.save(commit=True)
            doadora.save()
            messages.add_message(
                request, messages.SUCCESS, 'Doadora '+str(doadora.nome)+' adicionado com sucesso',
                fail_silently=True,
            )
            return redirect('/doadoras')
        else:
            messages.add_message(
                request, messages.ERROR, 'Formulario contem erros',
                fail_silently=True,
            )
            context = {
                'form_doadora': form_doadora,
                'form_endereco': form_endereco,
                'form_contato': form_contato,
            }
            return render(request, 'bdleite/add_doadora.html', context)

    else:
        form_doadora = DoadoraForm()
        form_endereco = EnderecoForm()
        form_contato = ContatoForm()

        context = {
            'form_doadora': form_doadora,
            'form_endereco': form_endereco,
            'form_contato': form_contato,
        }
    return render(request, 'bdleite/add_doadora.html', context)

@login_required
def edit_doadora(request, id_doadora):
    template = loader.get_template('bdleite/add_doadora.html')
    context = {
        'id': id_doadora,
    }
    return HttpResponse(template.render(context, request))

@login_required
def info_doadora(request, id_doadora):

    doadora = Doadora.objects.get(id=id_doadora)


    template = loader.get_template('bdleite/info_doadora.html')
    context = {
        'doadora': doadora,
    }
    return HttpResponse(template.render(context, request))

@login_required
def funcionarios(request):
    funcionarios = Funcionario.objects.all()
    template = loader.get_template('bdleite/funcionarios.html')
    context = {
        'funcionarios': funcionarios,
    }
    return HttpResponse(template.render(context, request))

@login_required
def add_funcionario(request):
    template = loader.get_template('bdleite/add_funcionario.html')
    context = {
        'teste': 'teste',
    }
    return HttpResponse(template.render(context, request))

@login_required
def edit_funcionario(request, id_funcionario):
    template = loader.get_template('bdleite/add_funcionario.html')
    context = {
        'teste': 'teste',
    }
    return HttpResponse(template.render(context, request))

@login_required
def info_funcionario(request, id_funcionario):
    template = loader.get_template('bdleite/info_funcionario.html')
    context = {
        'teste': 'teste',
    }
    return HttpResponse(template.render(context, request))

@login_required
def testes(request):
    template = loader.get_template('bdleite/testes.html')
    context = {
        'teste': 'teste',
    }
    return HttpResponse(template.render(context, request))