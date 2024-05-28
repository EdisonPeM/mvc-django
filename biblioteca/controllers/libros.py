from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.libros import LibrosModel

class LibrosController:
  def listar(request):
    libros = LibrosModel.listarLibros()
    alert = request.session.pop('alert', None)
    return render(request, "libros/listar.html", { 'libros': libros, 'alert': alert })
