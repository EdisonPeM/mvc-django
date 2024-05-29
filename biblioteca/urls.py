from django.urls import path, include

from .controllers.index import IndexController
from .controllers.autores import AutoresController
from .controllers.editoriales import EditorialesController

# Create url patterns
autoresPatterns = [
    path('', AutoresController.listar, name="listarAutores"),
    path('/nuevo', AutoresController.agregar, name="agregarAutor"),
    path('/editar/<str:codigo_autor>', AutoresController.editar, name="editarAutor"),
    path('/eliminar/<str:codigo_autor>', AutoresController.eliminar, name="eliminarAutor")
]

editorialesPatterns = [
    path('', EditorialesController.listar, name="listarEditoriales"),
    path('/nuevo', EditorialesController.agregar, name="agregarEditorial"),
    path('/editar/<str:codigo_editorial>', EditorialesController.editar, name="editarEditorial"),
    path('/eliminar/<str:codigo_editorial>', EditorialesController.eliminar, name="eliminarEditorial")
]

# Define Urls Patterns
urlpatterns = [
    path('', IndexController.home, name="home"),
    path('autores', include(autoresPatterns)),
    path('editoriales', include(editorialesPatterns)),
]