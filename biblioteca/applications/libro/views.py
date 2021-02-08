from django.shortcuts import render
from .models import Libro
from django.views.generic import ListView

# Create your views here

class ListLibros(ListView):
    template_name = 'libro/libros.html'
    context_object_name = 'listalibros'

    def get_queryset(self):
        palabraclave = self.request.GET.get('kword', '')
        f1 = self.request.GET.get('fecha1', '')
        f2 = self.request.GET.get('fecha2', '')
    
        if f1 and f2:
            return Libro.objects.listarlibrosfiltro(palabraclave, f1, f2)
        else:
            return Libro.objects.listaralllibros(palabraclave)


class ListLibros2categoria(ListView):
    template_name = 'libro/libros_bycategoria.html'
    context_object_name = 'listalibroscategoria'

    def get_queryset(self):
        palabraclave = self.request.GET.get('kword', '')
        if palabraclave:
            return Libro.objects.listar_libros_categoria(palabraclave)
        else:
            return Libro.objects.listar_libros_categoria(0)
