from django.contrib import admin

from bdleite.models import Funcionario, Doadora, Endereco, Contato

# Register your models here.

admin.site.register(Funcionario)
admin.site.register(Doadora)
admin.site.register(Endereco)
admin.site.register(Contato)