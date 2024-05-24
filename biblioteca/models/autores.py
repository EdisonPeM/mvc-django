from django.db import models

class Autor(models.Model):
  class Meta:
    db_table = 'autores'
  codigo_autor = models.CharField(max_length=6, primary_key=True)
  nombre_autor = models.CharField(max_length=50)
  nacionalidad = models.CharField(max_length=50)

class AutoresModel():
  def listarAutores():
    return Autor.objects.all()
  
  def insertarAutor(autor):
    try:
      autor.save(force_insert=True)
      return True
    except:
      return False
  
  def eliminarAutor(codigo):
    pass
  
  def modificarAutor(autor):
    try:
      autor.save(force_update=True)
      return True
    except:
      return False
  
  def obtenerAutor(codigo):
    try:
      return Autor.objects.get(codigo_autor=codigo)
    except Autor.DoesNotExist:
      return None

  def totalAutores():
    return len(Autor.objects.all())
