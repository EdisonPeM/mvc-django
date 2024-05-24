from django.http import Http404
from django.shortcuts import render

# Import Models
from ..models.autores import AutoresModel
from ..forms.autoresForm import AutoresForm

def listar(request):
  autores = AutoresModel.listarAutores()
  return render(request, "autores/list.html", { 'autores': autores })

def obtener(request, codigo_autor):
  autor = AutoresModel.obtenerAutor(codigo_autor)
  if autor:
    return render(request, "autores/detail.html", { "autor": autor })
  else:
    raise Http404("Autor does not exist")

def agregar(request):
  form = AutoresForm()
  return render(request, "autores/nuevo.html", { "form": form })

# def modificar(request):
#   modificar(request, response); 

# def eliminar(request):
#   eliminar(request, response);
