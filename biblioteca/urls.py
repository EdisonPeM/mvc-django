from django.urls import path, include

from .controllers import indexController, autoresController, generosController
from .controllers.index import IndexController
from .controllers.autores import AutoresController

# Create url patterns
autoresPatterns = [
    path('', AutoresController.listar, name="listarAutores"),
    path('/nuevo', AutoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', AutoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', AutoresController.eliminar, name="eliminarAutor")
]

generosPatterns = [
    path('', generosController.listar, name="listarGeneros"),
    path('/nuevo', generosController.agregar, name="agregarGenero"),
    path('/editar/<str:codigo_autor>', generosController.editar, name="editarGenero"),
    path('/eliminar/<str:codigo_autor>', generosController.eliminar, name="eliminarGenero")
]

urlpatterns = [
    path('', IndexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('generos', include(generosPatterns)),
]





