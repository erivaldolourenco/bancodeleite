import datetime

from django.contrib.auth import logout as dash_logout, authenticate, login as dash_login
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib import messages

from bdleite.models import Doadora


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
    template = loader.get_template('bdleite/add_doadora.html')
    context = {
        'teste': 'teste',
    }
    return HttpResponse(template.render(context, request))

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
    template = loader.get_template('bdleite/funcionarios.html')
    context = {
        'teste': 'teste',
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