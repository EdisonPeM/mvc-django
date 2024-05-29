from django.db import models
import traceback

class Genero(models.Model):
  class Meta:
    db_table = 'generos'
  id_genero = models.IntegerField(primary_key=True)
  nombre_genero = models.CharField(max_length=40)
  descripcion = models.CharField(max_length=100)
  
  def __str__(self):
    return self.nombre_genero
  
class GenerosModel():
  def listarGeneros():
    try:
      return Genero.objects.all()
    except:
      print(traceback.format_exc())
      return []
  
  def insertarGenero(genero):
    try:
      genero.save(force_insert=True)
      return True      
    except:
      print(traceback.format_exc())
      return False
  
  def obtenerGenero(id):
    try:
      return Genero.objects.get(id_genero=id)
    except Genero.DoesNotExist:
      print(traceback.format_exc())
      return None
  
  def modificarGenero(genero:Genero):
    try:
      genero.save(force_update=True)
      return True
    except:
      print(traceback.format_exc())
      return False
  
  def eliminarGenero(genero:Genero):
    try:
      genero.delete()
      return True
    except:
      print(traceback.format_exc())
      return False
  
  def totalGeneros():
    try:
      return Genero.objects.count()
    except:
      print(traceback.format_exc())
      return -1

