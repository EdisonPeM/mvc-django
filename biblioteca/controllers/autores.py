from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.autores import AutoresModel
from ..forms.autores import CrearAutoresForm, EditarAutoresForm

class AutoresController:
  def listar(request):
    autores = AutoresModel.listarAutores()
    alert = request.session.pop('alert', None)
    return render(request, "autores/listar.html", { 'autores': autores, 'alert': alert })

  def agregar(request):
    form = CrearAutoresForm()
    if request.method == 'POST':
      form = CrearAutoresForm(request.POST)
      if form.is_valid():
        autor = form.save(commit=False)
        if AutoresModel.insertarAutor(autor):
          request.session['alert'] = { 'type': 'success', 'message': 'El autor ha sido agregado exitosamente' }
        else:
          request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al agregar el autor' }
        return redirect('listarAutores')

    return render(request, "autores/agregar.html", { "form": form })

  def editar(request, codigo_autor):
    autor = AutoresModel.obtenerAutor(codigo_autor)
    if autor:
      form = EditarAutoresForm(instance=autor)
      if request.method == 'POST':
        form = EditarAutoresForm(request.POST, instance=autor)
        if form.is_valid():
          if AutoresModel.modificarAutor(autor):
            request.session['alert'] = { 'type': 'success', 'message': 'El autor ha sido actualizado exitosamente' }
          else:
            request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al actualizar el autor' }
          return redirect('listarAutores')

      return render(request, "autores/editar.html", { "autor": autor, "form": form })
    else:
      raise Http404("Autor does not exist")

  def eliminar(request, codigo_autor):
    if request.method == 'POST':
      autor = AutoresModel.obtenerAutor(codigo_autor)
      if autor:
        if AutoresModel.eliminarAutor(autor):
          request.session['alert'] = { 'type': 'success', 'message': 'El autor ha sido eliminado exitosamente' }
        else:
          request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al eliminar el autor' }

    return redirect('listarAutores')

