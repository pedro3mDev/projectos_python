from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from crud.views import index
from crud.views import listar
from crud.views import cadastrar
 
urlpatterns = [
    path('', index, name='rt_index'),
    path('listar/', listar, name='rt_listar'),
    path('cadastrar/', cadastrar, name='rt_cadastrar'),
]
