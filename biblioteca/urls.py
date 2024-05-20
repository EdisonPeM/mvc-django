from django.urls import path, include

from .controllers import autoresController

autoresPatterns = [
    path('', autoresController.listar, name="listarAutores"),
    path('/<str:codigo_autor>', autoresController.obtener, name="detalleAutor")
]

urlpatterns = [
    path('autores', include(autoresPatterns)),    
]