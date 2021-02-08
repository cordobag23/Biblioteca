from django.contrib import admin
from django.urls import path
from .import views

def hola(self):
    print('hola')
urlpatterns = [
    path('autores/', views.ListAutores.as_view(), name='autores'),
    
]
