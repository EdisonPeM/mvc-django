from django.db import models
import traceback

class Editorial(models.Model):
  class Meta:
    db_table = 'editoriales'
  codigo_editorial = models.CharField(max_length=6, primary_key=True)
  nombre_editorial = models.CharField(max_length=30)
  contacto = models.CharField(max_length=30)
  telefono = models.CharField(max_length=9)

  def __str__(self) -> str:
    return self.nombre_editorial


class EditorialModel():
  def listarEditoriales():
    try:
      return Editorial.objects.all()
    except:
      return []
  
  def obtenerEditorial(codigo):
    try:
      return Editorial.objects.get(codigo_editorial=codigo)
    except Editorial.DoesNotExist:
      return None
  
  def insertarEditorial(editorial):
    try:
      editorial.save(force_insert=True)
      return True
    except:
      return False
  
  def modificarEditorial(editorial):
    try:
      editorial.save(force_update=True)
      return True
    except:
      return False
  
  def eliminarEditorial(editorial):
    try:
      editorial.delete()
      return True
    except:
      return False
    
  def totalEditoriales():
    pass
