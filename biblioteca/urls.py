from django.urls import path, include

from .controllers import indexController, autoresController, generosController

autoresPatterns = [
    path('', autoresController.listar, name="listarAutores"),
    path('/nuevo', autoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', autoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', autoresController.eliminar, name="eliminarAutor")
]

generosPatterns = [
    path('', generosController.listar, name="listarGeneros"),
    path('/nuevo', generosController.agregar, name="agregarGenero"),
    path('/editar/<str:codigo_autor>', generosController.editar, name="editarGenero"),
    path('/eliminar/<str:codigo_autor>', generosController.eliminar, name="eliminarGenero")
]

urlpatterns = [
    path('', indexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('generos', include(generosPatterns)),
]





