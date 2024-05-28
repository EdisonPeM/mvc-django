from django.urls import path, include


from .controllers.index import IndexController
from .controllers.generosController import GenerosController
from .controllers.autores import AutoresController

# Create url patterns
autoresPatterns = [
    path('', AutoresController.listar, name="listarAutores"),
    path('/nuevo', AutoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', AutoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', AutoresController.eliminar, name="eliminarAutor")
]

generosPatterns = [
    path('', GenerosController.listar, name="listarGeneros"),
    path('/nuevo', GenerosController.agregar, name="agregarGenero"),
    path('/editar/<str:codigo_genero>', GenerosController.editar, name="editarGenero"),
    path('/eliminar/<str:codigo_genero>', GenerosController.eliminar, name="eliminarGenero")
]

urlpatterns = [
    path('', IndexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('generos', include(generosPatterns)),
]





