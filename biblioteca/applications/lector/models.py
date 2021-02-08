from django.db import models
from applications.libro.models import Libro
# Create your models here.
class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=30)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.nombre

    
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    #la fecha d devolucion se actualiza cuando el lobo es dfevuelto
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    def __str__(self):
        return self.libro.titulo



