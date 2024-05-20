from django.db import models

class Autores(models.Model):
  codigo_autor = models.CharField(max_length=6, primary_key=True)
  nombre_autor = models.CharField(max_length=50)
  nacionalidad = models.CharField(max_length=50)
  
  def listarAutores():
    return Autores.objects.all()
  
  def insertarAutor(autor):
    pass
  
  def eliminarAutor(codigo):
    pass
  
  def modificarAutor(autor):
    pass
  
  def obtenerAutor(codigo):
    return Autores.objects.get(codigo_autor=codigo)

  def totalAutores():
    return len(Autores.objects.all())
