from django.core.validators import RegexValidator
from django import forms

from .baseForm import BaseModelForm

from ..models.editoriales import Editorial

codigo_editorial_validator = RegexValidator(
    regex=r'^EDI\d{3}$',
    message="Ingrese un código valido en formato EDI123",
    code="invalid_editorial_code"
)

labels = {
    'codigo_editorial': 'Código de la editorial',
    'nombre_editorial': 'Nombre de la editorial',
    'contacto': 'Contacto de la editorial',
    'telefono': 'Numero de telefono'
}

class CrearEditorialesForm(BaseModelForm):
    codigo_editorial = forms.CharField(
        label=labels["codigo_editorial"],
        max_length=6,
        required=True,
        validators=[codigo_editorial_validator]
    )

    class Meta():
        model = Editorial
        fields = "__all__"
        labels = labels

class EditarEditorialesForm(BaseModelForm):
    class Meta():
        model = Editorial
        fields = ["nombre_editorial", "contacto", "telefono"]
        labels = labels