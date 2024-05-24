from django.core.validators import RegexValidator
from django import forms

from ..models.autores import Autor

codigo_autor_validator = RegexValidator(
  regex=r'^AUT\d{3}$',
  message="Ingrese un código valido en formato AUT123.",
  code="invalid_autor_code",
)

labels = {
  'codigo_autor': 'Código del Autor',
  'nombre_autor': 'Nombre del Autor',
  'nacionalidad': 'Nacionalidad'
}

class CrearAutoresForm(forms.ModelForm):
  template_name = "bs-form.html" 
  
  codigo_autor = forms.CharField(
    label=labels["codigo_autor"],
    max_length=6,
    required=True,
    validators=[codigo_autor_validator]
  )

  class Meta():
    model = Autor
    fields = "__all__"
    labels = labels

    
class EditarAutoresForm(forms.ModelForm):
  template_name = "bs-form.html" 

  class Meta():
    model = Autor
    fields = ["nombre_autor", "nacionalidad"]
    labels = labels