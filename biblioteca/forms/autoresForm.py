from django.core.validators import RegexValidator
from django import forms

codigo_autor_validator = RegexValidator(
  regex=r'^AUT\d{3}$',
  message="Ingrese un código valido en formato AUT123.",
  code="invalid_autor_code",
)

class AutoresForm(forms.Form):
  template_name = "bs-form.html" 
  
  codigo = forms.CharField(label="Código del Autor", max_length=6, required=True, validators=[codigo_autor_validator])
  nombre = forms.CharField(label="Nombre del Autor", max_length=50, required=True)
  nacionalidad = forms.CharField(label="Nacionalidad", max_length=50, required=True)