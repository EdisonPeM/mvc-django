from django.http import Http404
from django.shortcuts import render

# Import Models
from ..models.autores import Autores

def listar(request):
  return render(request, "autores/list.html", { 'autores': Autores.listarAutores() })

def obtener(request, codigo_autor):
  try:
    autor = Autores.obtenerAutor(codigo_autor)
    return render(request, "autores/detail.html", { "autor": autor })
  
  except Autores.DoesNotExist:
    raise Http404("Autor does not exist")

# def nuevo(request):
#   request.getRequestDispatcher("/autores/nuevoAutor.jsp").forward(request, response); 

# def insertar(request):
#   insertar(request, response); 

# def modificar(request):
#   modificar(request, response); 

# def eliminar(request):
#   eliminar(request, response);