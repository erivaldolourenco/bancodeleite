"""bancodeleite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from bdleite import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('doadoras', views.doadoras, name='listar-doadoras'),
    path('doadoras/add', views.add_doadora, name='adicionar-doadora'),
    path('doadoras/<int:id_doadora>', views.info_doadora, name='informacao-doadora'),
    path('doadoras/<int:id_doadora>/edit', views.edit_doadora, name='editar-doadora'),

    path('funcionarios', views.funcionarios, name='listar-funcionarios'),
    path('funcionarios/add', views.add_funcionario, name='adicionar-funcionario'),
    path('funcionarios/<int:id_funcionario>', views.info_funcionario, name='informacao-funcionario'),
    path('funcionarios/<int:id_funcionario>/edit', views.edit_funcionario, name='editar-funcionario'),

    path('testes', views.testes, name='testes')
]