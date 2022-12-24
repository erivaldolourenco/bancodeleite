
from django import forms
from django.contrib.auth.models import User
from django.forms import ModelForm, TextInput ,Textarea, FileInput, SelectMultiple, DateField, CheckboxSelectMultiple, CheckboxInput

from bdleite.models import Doadora, Endereco, Contato


class DoadoraForm(ModelForm):
    class Meta:
        model = Doadora
        fields = ('nome', 'sobrenome')
        labels = {
            'nome': 'Nome',
            'sobrenome': 'Sobrenome'
        }
        widgets = {
            'nome': TextInput(attrs={'class': "form-control"}),
            'sobrenome': TextInput(attrs={'class': "form-control"}),
        }


class EnderecoForm(ModelForm):
    class Meta:
        model = Endereco
        fields = ('rua', 'bairro','cidade','estado', 'cep')
        labels = {
            'rua':'Endereco',
            'bairro':'Bairro',
            'cidade':'Cidade',
            'estado':'UF',
            'cep':'CEP'
        }

        widgets = {
            'rua': TextInput(attrs={'class': "form-control"}),
            'bairro': TextInput(attrs={'class': "form-control"}),
            'cidade': TextInput(attrs={'class': "form-control"}),
            'estado': TextInput(attrs={'class': "form-control"}),
            'cep': TextInput(attrs={'class': "form-control"}),
        }

class ContatoForm(ModelForm):
    class Meta:
        model = Contato
        fields = ('telefone', 'celular')
        labels = {
            'telefone': 'Telefone',
            'celular' : 'Celular'
        }
        widgets = {
            'telefone': TextInput(attrs={'class': "form-control"}),
            'celular': TextInput(attrs={'class': "form-control"})
        }
