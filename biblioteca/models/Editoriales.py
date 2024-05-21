from django.db import models

class Editorial(models.Model):
  class Meta:
    db_table = 'editoriales'
  codigo_editorial = models.CharField(max_length=6, primary_key=True)
  nombre_editorial = models.CharField(max_length=30)
  contacto = models.CharField(max_length=30)
  telefono = models.CharField(max_length=9)
  
  
class EditorialModel():
  def listarEditoriales():
    pass
  
  def insertarEditorial(editorial):
    pass
  
  def obtenerEditorial(codigo):
    pass
  
  def modificarEditorial(editorial):
    pass
  
  def eliminarEditorial(codigo):
    pass
  
  def totalEditoriales():
    pass
