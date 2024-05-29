from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.libros import LibrosModel
from ..forms.libros import CrearLibrosForm, EditarLibrosForm

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

  def editar(request, codigo_libro):
    libro = LibrosModel.obtenerLibro(codigo_libro)
    if libro:
      form = EditarLibrosForm(instance=libro)
      if request.method == 'POST':
        form = EditarLibrosForm(request.POST, instance=libro)
        if form.is_valid():
          if LibrosModel.modificarLibro(libro):
            request.session['alert'] = { 'type': 'success', 'message': 'El libro ha sido actualizado exitosamente' }
          else:
            request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al actualizar el libro' }
          return redirect('listarLibros')

      return render(request, "libros/editar.html", { "libro": libro, "form": form })
    else:
      raise Http404("Libro does not exist")