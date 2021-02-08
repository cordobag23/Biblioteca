from django.shortcuts import render
from django.views.generic import ListView
# modelos local
from .models import Autor


class ListAutores(ListView):
    context_object_name = 'lista_autores'
    template_name = "autor/lista.html"

    def get_queryset(self):
        palabraclave = self.request.GET.get('kword', '')
        #le mando la funcion de managerautor    listar_autores()
        return Autor.objects.buscarautor4(palabraclave)
        
       
