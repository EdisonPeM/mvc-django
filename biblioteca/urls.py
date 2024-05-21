from django.urls import path, include

from .controllers import autoresController

autoresPatterns = [
    path('', autoresController.listar, name="listarAutores"),
    path('/nuevo', autoresController.agregar, name="agregarAutor"),
    path('/detalle/<str:codigo_autor>', autoresController.obtener, name="detalleAutor"),
    # path('/editar/<str:codigo_autor>', autoresController.obtener, name="editarAutor"),
    # path('/eliminar/<str:codigo_autor>', autoresController.obtener, name="eliminarAutor")
]

urlpatterns = [
    path('autores', include(autoresPatterns)),    
]