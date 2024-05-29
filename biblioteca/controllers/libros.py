from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.libros import LibrosModel
from ..forms.libros import CrearLibrosForm

class LibrosController:
  def listar(request):
    libros = LibrosModel.listarLibros()
    alert = request.session.pop('alert', None)
    return render(request, "libros/listar.html", { 'libros': libros, 'alert': alert })

  def agregar(request):
    form = CrearLibrosForm()
    return render(request, "libros/agregar.html", { "form": form })
