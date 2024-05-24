from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.autores import AutoresModel, Autor
from ..forms.autoresForm import CrearAutoresForm, EditarAutoresForm

def listar(request):
  autores = AutoresModel.listarAutores()
  return render(request, "autores/list.html", { 'autores': autores })

def agregar(request):
  form = CrearAutoresForm()
  if request.method == 'POST':
    form = CrearAutoresForm(request.POST)
    if form.is_valid():
      autor = form.save(commit=False)
      AutoresModel.insertarAutor(autor)
      return redirect('listarAutores')

  return render(request, "autores/nuevo.html", { "form": form })

def editar(request, codigo_autor):
  autor = AutoresModel.obtenerAutor(codigo_autor)
  if autor:
    form = EditarAutoresForm(instance=autor)
    if request.method == 'POST':
      form = EditarAutoresForm(request.POST, instance=autor)
      if form.is_valid():
        AutoresModel.modificarAutor(autor)
        return redirect('listarAutores')

    return render(request, "autores/editar.html", { "autor": autor, "form": form })
  else:
    raise Http404("Autor does not exist")

# def eliminar(request):
#   eliminar(request, response);
