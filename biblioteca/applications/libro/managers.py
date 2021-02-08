#importo datetime para poder ocnvertir mis fechas en el format A/M/D
import datetime
#aqui creo mis propias consultas a mi base de datos(importo mis modelos)
from django.db import models
from django.db.models import Q


class LibroManager(models.Manager):

    def listaralllibros(self, kword):
        #listamos y filtram}os libros po
        # titulo Y (recordr q la y se represn con ,) rango de fecha
        filtro = self.filter(
            titulo__icontains=kword
        )
        return filtro

    
    def listarlibrosfiltro(self, kword, fecha1, fecha2):
        #le damos formato A/M/D, de string a fecha
        date1 = datetime.datetime.strptime(fecha1, '%Y-%m-%d').date() 
        date2 = datetime.datetime.strptime(fecha2, '%Y-%m-%d').date() 
        #listamos y filtram}os libros po
        # titulo Y (recordr q la y se represn con ,) rango de fecha
        filtro = self.filter(
            titulo__icontains=kword, 
            fecha__range = (date1, date2)
        )
        return filtro
    
    def listar_libros_categoria(self, categoria):
        return self.filter(
            categoria__id=categoria
        ).order_by('titulo')

#lista las categorias de los autores de los libros
#relacionando la categoria a traves de un related_name -->"categorialibro"
# en el mopdelos libro
class CategoriaManager(models.Manager):
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct() # que no me traoiga datos repetidos, es decir si tiene
        #varios lisbros en una misma categoria, q solo me traiga esa categoria una sola vez

