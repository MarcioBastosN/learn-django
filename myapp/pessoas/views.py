from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render

from django.views import generic
from .models import Pessoa

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'pessoas/index.html'
    # context_object_name = 'pessoas'
    def get_queryset(self):
        return Pessoa.objects.all()
    
class HomenView(generic.ListView):
    template_name = 'pessoas/showman.html'
    
    def get_queryset(self):
        # return Pessoa.objects.filter(genero= 'm')
        return Pessoa.objects.masculino()

class MulhersView(generic.ListView):
    template_name = 'pessoas/showwoman.html'
    
    def get_queryset(self):
        return Pessoa.objects.filter(genero= 'f')
    
class GenerosView(generic.ListView):
    
    template_name = 'pessoas/index.html'

    def get_context_data(self, **kwargs):
        return Pessoa.objects.filter(genero = kwargs['genero'])