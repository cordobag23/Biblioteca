#importo datetime para poder ocnvertir mis fechas en el format A/M/D
import datetime
#aqui creo mis propias consultas a mi base de datos(importo mis modelos)
from django.db import models
from django.db.models import Q, Count


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

    #agregar a un libro otro autor q ya este creado, desde el codigo
    def agregar_libro(self, libro_id, autor):
        libro = self.get(id=libro_id)
        libro.autores.add(autor)
        return libro

    # similar abajo, el numero de veces q fue prestado un libro pero con Aggregate
    def libros_num_prestmo(self):
        resultado = self.aggregate(
            #recuerda, si notienes relacion con el otro odelo
            # utiliza el related-name
            plr=Count('prestamo_libro')
        )   
        #devuelve un diccionario clave:valor , con el valor de la operacion aritmetica--encuentra un valor
        return resultado

#lista las categorias de los autores de los libros
#relacionando la categoria a traves de un related_name -->"categorialibro"
# en el mopdelos libro
class CategoriaManager(models.Manager):
    
    def categoria_por_autor(self, autor):
        return self.filter(
            categoria_libro__autores__id=autor
        ).distinct() # que no me traoiga datos repetidos, es decir si tiene
        #varios lisbros en una misma categoria, q solo me traiga esa categoria una sola vez


    #bamos a contar cuantos librs tiene cada categoria
    def contar_libr_by_categori(self):
        resultado = self.annotate(
            #contamos los libros, q atributo queremos contyar del modelo categoria
            # es decir la cantidad de libros q tiene cada categoria, pero como no estan relacionados
            #categoria con libro, utilizo el related_name--- categoria_libro
            num_libr= Count('categoria_libro')
            # devuelve un queryset con una columna nueva eje.  num_libro y su valor
        )
        return resultado #si deseara tilizarla sin v¿una vista, la itero  con un for x in resultado

    

      




