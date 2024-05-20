from django.db import models


class Autores(models.Model):
  codigo_autor = models.CharField(max_length=6, primary_key=True)
  nombre_autor = models.CharField(max_length=50)
  nacionalidad = models.CharField(max_length=50)

class Generos(models.Model):
  id_genero = models.IntegerField(primary_key=True)
  nombre_genero = models.CharField(max_length=40)
  descripcion = models.CharField(max_length=100)

class Editoriales(models.Model):
  codigo_editorial = models.CharField(max_length=6, primary_key=True)
  nombre_editorial = models.CharField(max_length=30)
  contacto = models.CharField(max_length=30)
  telefono = models.CharField(max_length=9)

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
  