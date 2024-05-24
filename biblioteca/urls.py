from django.urls import path, include

from .controllers import indexController, autoresController

autoresPatterns = [
    path('', autoresController.listar, name="listarAutores"),
    path('/nuevo', autoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', autoresController.editar, name="editarAutor"),
    # path('/eliminar/<str:codigo_autor>', autoresController.obtener, name="eliminarAutor")
]

urlpatterns = [
    path('', indexController.home, name="home"),
    path('autores', include(autoresPatterns)),
]