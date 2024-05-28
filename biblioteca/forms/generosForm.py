from django.core.validators import RegexValidator
from django import forms

from .baseForm import BaseModelForm
from ..models.generos import Genero

codigo_autor_validator = RegexValidator(
  message="Ingrese un código valido en formato 12323.",
  code="invalid_autor_code",
)

labels = {
  'id_genero': 'Código de genero',
  'nombre_genero': 'Nombre del genero',
  'descripcion': 'Descripción'
}

class CrearGenerosForm(BaseModelForm):
  id_genero = forms.CharField(
    label=labels["id_genero"],
    max_length=6,
    required=True,
    validators=[codigo_autor_validator]
  )

  class Meta():
    model = Genero
    fields = "__all__"
    labels = labels

    
class EditarGenerosForm(BaseModelForm):
  class Meta():
    model = Genero
    fields = ["nombre_genero", "descripcion"]
    labels = labels