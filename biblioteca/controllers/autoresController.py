from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.autores import AutoresModel, Autor
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
  if request.method == 'POST':
    form = AutoresForm(request.POST)
    if form.is_valid():
      autor = Autor(
        codigo_autor=request.POST['codigo'],
        nombre_autor=request.POST['nombre'],
        nacionalidad=request.POST['nacionalidad']
      )

      AutoresModel.insertarAutor(autor)
      return redirect('listarAutores')

  return render(request, "autores/nuevo.html", { "form": form })

# def modificar(request):
#   modificar(request, response); 

# def eliminar(request):
#   eliminar(request, response);
