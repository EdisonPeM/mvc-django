from django.db import models


from .autores import Autor
from .editoriales import Editorial
from .generos import Genero

class Libro(models.Model):
  class Meta:
    db_table = 'libros'
  codigo_libro = models.CharField(max_length=9, primary_key=True)
  nombre_libro = models.CharField(max_length=50)
  descripcion = models.TextField()
  # Foreign Keys
  codigo_autor = models.ForeignKey(Autor, on_delete=models.CASCADE)
  codigo_editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE)
  id_genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
  # Biblioteca Data
  existencias = models.PositiveIntegerField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  
class LibrosModel():
  def listarLibros():
    try:
      return Libro.objects.all()
    except:
      return []
  
  def obtenerLibro(codigo):
    pass
  
  def insertarLibro(libro):
    try:
      libro.save(force_insert=True)
      return True
    except:
      return False
  
  def modificarLibro(libro):
    pass
  
  def eliminarLibro(codigo):
    pass 
