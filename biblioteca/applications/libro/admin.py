from django.contrib import admin
from . models import *
# Register your models here.

class LibroAdmin(admin.ModelAdmin):
    filter_horizontal = ('autores',)

admin.site.register(Categoria)
admin.site.register(Libro, LibroAdmin)