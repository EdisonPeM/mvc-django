from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.generos import GenerosModel
from ..forms.generosForm import CrearGenerosForm, EditarGenerosForm
class GenerosController:

  def listar(request):
    generos = GenerosModel.listarGeneros()
    alert = request.session.pop('alert', None)
    return render(request, "generos/listar.html", { 'generos': generos, 'alert': alert })

  def agregar(request):
    form = CrearGenerosForm()
    if request.method == 'POST':
      form = CrearGenerosForm(request.POST)
      if form.is_valid():
        genero = form.save(commit=False)
        if GenerosModel.insertarGenero(genero):
          request.session['alert'] = { 'type': 'success', 'message': 'El genero ha sido agregado exitosamente' }
        else:
          request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al agregar el genero' }
        return redirect('listarGeneros')

    return render(request, "generos/agregar.html", { "form": form })

  def editar(request, id_genero:int):
    genero = GenerosModel.obtenerGenero(id_genero)
    if genero:
      form = EditarGenerosForm(instance=genero)
      if request.method == 'POST':
        form = EditarGenerosForm(request.POST, instance=genero)
        if form.is_valid():
          if GenerosModel.modificarGenero(genero):
            request.session['alert'] = { 'type': 'success', 'message': 'El genero ha sido actualizado exitosamente' }
          else:
            request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al actualizar el genero' }
          return redirect('listarGeneros')

      return render(request, "generos/editar.html", { "autor": genero, "form": form })
    else:
      raise Http404("Generos does not exist")

  def eliminar(request, id_genero):
    print("entraa", id_genero)
    if request.method == 'POST':
      genero = GenerosModel.obtenerGenero(id_genero)
      if genero:
        if GenerosModel.eliminarGenero(genero):
          request.session['alert'] = { 'type': 'success', 'message': 'El genero ha sido eliminado exitosamente' }
        else:
          request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al eliminar el genero' }

    return redirect('listarGeneros')