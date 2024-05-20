from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
  return HttpResponse("Hello, world. You're in the Biblioteca index.")

def detail(request, some_id):
  context = { 'some_id': some_id }
  return render(request, "index.html", context)
  
# def insertar():
#   insertar(request, response); break; 

# def obtener():
#   obtener(request, response); break; 

# def modificar():
#   modificar(request, response); break; 

# def eliminar():
#   eliminar(request, response); break; 