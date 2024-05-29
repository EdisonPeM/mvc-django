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
  autor = models.ForeignKey(Autor, on_delete=models.CASCADE, db_column='codigo_autor', related_name='libros')
  genero = models.ForeignKey(Genero, on_delete=models.CASCADE, db_column='id_genero', related_name='libros')
  editorial = models.ForeignKey(Editorial, on_delete=models.CASCADE, db_column='codigo_editorial', related_name='libros')
  # Biblioteca Data
  existencias = models.PositiveIntegerField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  
  def __str__(self):
    # set string format as 'nombre_libro, nombre_autor'
    return f'{self.nombre_libro}, {self.autor.nombre_autor}'
  
class LibrosModel():
  def listarLibros():
    try:
      return Libro.objects.all()
    except:
      return []
  
  def obtenerLibro(codigo):
    try:
      return Libro.objects.get(codigo_libro=codigo)
    except Libro.DoesNotExist:
      return None
  
  def insertarLibro(libro):
    try:
      libro.save(force_insert=True)
      return True
    except:
      return False
  
  def modificarLibro(libro):
    try:
      libro.save(force_update=True)
      return True
    except:
      return False
  
  def eliminarLibro(libro):
    try:
      libro.delete()
      return True
    except:
      return False
