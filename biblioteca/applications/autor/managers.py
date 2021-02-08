

#aqui creo mis propias consultas a mi base de datos(importo mis modelos)
from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    """managers para el modelo autor"""
    # para decirle a q autor prtenece madndo la clase a los modelos
    def buscarautor(self, kword):
        resultado = self.filter(nombre__icontains=kword)
        return resultado
    
    #al mismo modelo, le otorgoo una consulta como sifuera lenguaje sql
    # and or(import Q) y otrros, hago cuantas funciones de consulta necesite

    def consultar2(self, kword):
        #quiero q envies la consult cuyo nombre o apellido coincidan con la busqueda
        resultado = self.filter(
            Q(nombre__icontains=kword) | Q(apellidos__icontains=kword)
        )
        return resultado
        #quiero q envies la consult cuyo nombre o apellido coincidan con la busqueda
        #pero q excluya a los q su edad sea igual a 35
    def buscarautor3(self, kword):
        resultado = self.filter(nombre__icontains=kword).exclude(edad=4)
        return resultado

    def buscarautor4(self, kword):
        resultado = self.filter(
            nombre__icontains=kword,
            edad__gt=4

        )
        #mayor que se respresnta: gt   
        #menor que se represneta: it
        #indicar Y se represneta: ,
        return resultado



    

