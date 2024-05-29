from django.core.validators import RegexValidator
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

codigo_libro_field = forms.CharField(
  label=labels["codigo_libro"],
  max_length=6,
  required=True,
  validators=[
    RegexValidator(
      regex=r'^LIB\d{3}$',
      message="Ingrese un código valido en formato LIB000.",
      code="invalid_libro_code",
    )
  ]
)

precio_field = forms.DecimalField(
  required=True,
  max_digits=10,
  decimal_places=2,
  min_value=0,
  label=labels["precio"],
  help_text = "En pesos colombianos",
)
# Additional symbol to show in the UI
precio_field.prefix = '$'

class CrearLibrosForm(BaseModelForm):
  codigo_libro = codigo_libro_field
  precio = precio_field
  
  class Meta():
    model = Libro
    fields = "__all__"
    labels = labels
    
class EditarLibrosForm(BaseModelForm):
  precio = precio_field

  class Meta():
    model = Libro
    exclude = ["codigo_libro"]
    labels = labels