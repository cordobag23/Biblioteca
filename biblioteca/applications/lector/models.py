from django.db import models
from applications.libro.models import Libro
from .managers import PrestamoManager
# Create your models here.
class Lector(models.Model):
    nombre = models.CharField('Nombre', max_length=50)
    apellidos = models.CharField('Apellidos', max_length=50)
    nacionalidad = models.CharField('Nacionalidad', max_length=30)
    edad = models.PositiveIntegerField(default=0)

    def __str__(self):
        return str(self.id) + ' ' + self.nombre

    
class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE, related_name = 'prestamo_libro')
    #la fecha d devolucion se actualiza cuando el lobo es dfevuelto
    fecha_prestamo = models.DateField()
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()
    objects = PrestamoManager()

    def __str__(self):
        return str(self.id) + ' ' + self.libro.titulo



