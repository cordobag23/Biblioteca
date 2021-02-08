from django.db import models
#importo el manager para autor.... hacer la consulta a la bd
# entre los atributos del modelo, conecto mi manager con su modelo, a trave del campo... objects = AutorManager
#esto lo recibe tambn la vista, pero solo le damos el nimbre de la funcion
from .managers import AutorManager
# Create your models here.

class Autor(models.Model):
    nombre = models.CharField('Nombre', 
        max_length=50
    )
    apellidos = models.CharField('Apellidos', 
        max_length=50
    )
    nacionalidad = models.CharField('Nacionalidad', 
        max_length=30
    )
    edad = models.PositiveIntegerField()
    objects = AutorManager()
  

    def __str__(self):
        return str(self.id) + ' - ' +self.nombre + ' ' + self.apellidos
