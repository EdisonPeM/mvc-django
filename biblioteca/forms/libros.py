from django import forms

from .baseForm import BaseModelForm

from ..models.libros import Libro

labels = {
  'codigo_libro': 'Código del Libro',
  'nombre_libro': 'Nombre del Libro',
  'existencias': 'Existencias',
  'precio': 'Precio',
  'descripcion': 'Descripción',
  'codigo_autor': 'Autor',
  'codigo_editorial': 'Editorial',
  'id_genero': 'Genero'
}

precioField = forms.DecimalField(
  required=True,
  max_digits=10,
  decimal_places=2,
  min_value=0,
  label=labels["precio"],
  help_text = "En pesos colombianos",
)
# Additional symbol to show in the UI
precioField.prefix = '$'

class CrearLibrosForm(BaseModelForm):
  precio = precioField
  
  class Meta():
    model = Libro
    fields = "__all__"
    labels = labels
    
class EditarLibrosForm(BaseModelForm):
  precio = precioField

  class Meta():
    model = Libro
    exclude = ["codigo_libro"]
    labels = labels