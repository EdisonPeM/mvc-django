from django.http import Http404
from django.shortcuts import render

# Import Models
from ..models.autores import AutoresModel

def listar(request):
  autores = AutoresModel.listarAutores()
  return render(request, "autores/list.html", { 'autores': autores })

def obtener(request, codigo_autor):
  autor = AutoresModel.obtenerAutor(codigo_autor)
  if autor:  
    return render(request, "autores/detail.html", { "autor": autor })
  else:
    raise Http404("Autor does not exist")

# def nuevo(request):
#   request.getRequestDispatcher("/autores/nuevoAutor.jsp").forward(request, response); 

# def insertar(request):
#   insertar(request, response); 

# def modificar(request):
#   modificar(request, response); 

# def eliminar(request):
#   eliminar(request, response);