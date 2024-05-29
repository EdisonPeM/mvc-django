from django.urls import path, include


from .controllers.index import IndexController
from .controllers.generos import GenerosController
from .controllers.autores import AutoresController
from .controllers.libros import LibrosController

# Create Autores url patterns
autoresPatterns = [
    path('', AutoresController.listar, name="listarAutores"),
    path('/nuevo', AutoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', AutoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', AutoresController.eliminar, name="eliminarAutor")
]
 
# Create Generos url patterns
generosPatterns = [
    path('', GenerosController.listar, name="listarGeneros"),
    path('/nuevo', GenerosController.agregar, name="agregarGenero"),
    path('/editar/<str:id_genero>', GenerosController.editar, name="editarGenero"),
    path('/eliminar/<str:id_genero>', GenerosController.eliminar, name="eliminarGenero")
]

# Create Libros url patterns
librosPatterns = [
    path('', LibrosController.listar, name="listarLibros"),
    path('/nuevo', LibrosController.agregar, name="agregarLibro"),
    path('/editar/<str:codigo_libro>', LibrosController.editar, name="editarLibro"),
    path('/eliminar/<str:codigo_libro>', LibrosController.eliminar, name="eliminarLibro")
]

# Define Urls Patterns
urlpatterns = [
    path('', IndexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('generos', include(generosPatterns)),
    path('libros', include(librosPatterns)),
]
