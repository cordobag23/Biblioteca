from django.contrib import admin
from django.urls import path
from .import views

def hola(self):
    print('hola')
urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros_categoria/', views.ListLibros2categoria.as_view(), name='librosxcategoria'),
    path('detalle_lib/<pk>/', views.Detalle_librDetailView.as_view(), name='detallelibro'),
    
]
