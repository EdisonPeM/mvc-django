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
    if request.method == 'POST':
      form = CrearLibrosForm(request.POST)
      if form.is_valid():
        libro = form.save(commit=False)
        if LibrosModel.insertarLibro(libro):
          request.session['alert'] = { 'type': 'success', 'message': 'El libro ha sido agregado exitosamente' }
        else:
          request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al agregar el libro' }
        return redirect('listarLibros')

    return render(request, "libros/agregar.html", { "form": form })
