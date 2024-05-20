from django.db import models


from .Autores import Autores
from .Editoriales import Editoriales
from .Generos import Generos

class Libros(models.Model):
  codigo_libro = models.CharField(max_length=9, primary_key=True)
  nombre_libro = models.CharField(max_length=50)
  existencias = models.IntegerField()
  precio = models.DecimalField(max_digits=10, decimal_places=2)
  descripcion = models.TextField()
  # Foreign Keys
  codigo_autor = models.ForeignKey(Autores, on_delete=models.CASCADE)
  codigo_editorial = models.ForeignKey(Editoriales, on_delete=models.CASCADE)
  id_genero = models.ForeignKey(Generos, on_delete=models.CASCADE)
  
  def listarLibros():
    pass
  
  def insertarLibro(Libro):
    pass
  
  def obtenerLibro(codigo):
    pass
  
  def modificarLibro(libro):
    pass
  
  def eliminarLibro(codigo):
    pass 
  
  def totalLibros():
    pass