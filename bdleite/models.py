import os

from django.contrib.auth.models import User
from django.db import models
from django.utils.crypto import get_random_string


# Create your models here.

def rename_img_profile(instance, filename):
    path = 'profiles/'
    # print(dir(instance))
    file_name = '{0}_{1}.{2}'.format(instance, get_random_string(length=32), filename.split(".")[-1])
    return os.path.join(path, file_name)

class Endereco(models.Model):
    rua = models.CharField(max_length=200)
    bairro = models.CharField(max_length=100)
    cidade = models.CharField(max_length=50)
    estado = models.CharField(max_length=30)
    cep = models.CharField(max_length=10)
    def __str__(self):
        return str(self.cep)
class Contato(models.Model):
    telefone = models.CharField(max_length=11,null=True, blank=True)
    celular = models.CharField(max_length=11,null=True, blank=True)
    def __str__(self):
        return str(self.telefone)

class Doadora(models.Model):
    nome = models.CharField(max_length=200)
    sobrenome = models.CharField(max_length=200)
    endereco = models.ForeignKey(Endereco,null=True, blank=True, on_delete=models.SET_NULL)
    contato = models.ForeignKey(Contato,null=True, blank=True, on_delete=models.SET_NULL)
    def __str__(self):
        return str(self.nome)

class Funcionario(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to=rename_img_profile, blank=True, null=True)

    def __str__(self):
        return self.user.first_name