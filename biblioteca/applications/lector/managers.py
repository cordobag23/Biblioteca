#importo datetime para poder ocnvertir mis fechas en el format A/M/D
import datetime
#aqui creo mis propias consultas a mi base de datos(importo mis modelos)
from django.db import models
from django.db.models import Q, Count
from django.db.models.aggregates import Avg
from django.db.models.functions import Lower

class PrestamoManager(models.Manager):

    #promedio de edades d los lectores q prestaron el libro X

    def promedio_edad_librox(self):
        #filtro todos los prerstamos del libro x de id 
        resultado = self.filter(
            libro__id= 2

        ).aggregate(
            promedioedad=Avg('lector__edad'),
            #si quiero seguir agregado consultas aritmeticas coloco la coma de rriba , y
            #sigo afrebagdo:
            suma_todas_las_edades_ = Sum('lector__edad')
        # Avg  ---> manda el promedio de lo q le mandemos como parametro
        )# aplica la funcion agregate para q calcule el promedio de edades
          # de los lectores q prestaron ese libro
        return resultado


#numero de libros prestados, es decir si tiene una lista l1, l2, l1, l3, l1, lo correcto seria:
# l1 = 3
# l2 = 1
# l3 = 1
    def mun_libro_prestados(self):
        result = self.values(
            'libro'
            # °arriba!en base a qu valores quiero el annonate
            #comienz¿ce a contar libros?? en base a cada registr d libro
            #este values devuelve dicionarios___  [{}, {}, {}]
        ).annotate(
            numprest=Count('libro'), #agregamos q traiga el titulo
            titulol = Lower('libro__titulo')
        )#nos devolveria un diccionario, para acceder  aun diccionario con un for r['']
        for r in result:
            print(r, r['numprest'])
        return result