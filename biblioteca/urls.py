from django.urls import path, include

from .controllers.index import IndexController
from .controllers.autores import AutoresController
from .controllers.libros import LibrosController

# Create url patterns
autoresPatterns = [
    path('', AutoresController.listar, name="listarAutores"),
    path('/nuevo', AutoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', AutoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', AutoresController.eliminar, name="eliminarAutor")
]

# Create libros url patterns
librosPatterns = [
    path('', LibrosController.listar, name="listarLibros"),
    # path('/nuevo', LibrosController.agregar, name="agregarAutor"),
    # path('/editar/<str:codigo_autor>', LibrosController.editar, name="editarAutor"),
    # path('/eliminar/<str:codigo_autor>', LibrosController.eliminar, name="eliminarAutor")
]
 
# Define Urls Patterns
urlpatterns = [
    path('', IndexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('libros', include(librosPatterns)),
]