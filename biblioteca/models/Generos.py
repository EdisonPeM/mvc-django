from django.db import models

class Generos(models.Model):
  id_genero = models.IntegerField(primary_key=True)
  nombre_genero = models.CharField(max_length=40)
  descripcion = models.CharField(max_length=100)
  
  def listarGeneros():
    pass
  
  def insertarGenero(genero):
    pass
  
  def obtenerGenero(id):
    pass
  
  def modificarGenero(genero):
    pass
  
  def eliminarGenero(id):
    pass
  
  def totalGeneros():
    pass

