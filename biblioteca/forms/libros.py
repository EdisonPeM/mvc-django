from .baseForm import BaseModelForm

from ..models.libros import Libro

class CrearLibrosForm(BaseModelForm):
  class Meta():
    model = Libro
    fields = "__all__"
    
class EditarLibrosForm(BaseModelForm):
  class Meta():
    model = Libro
    exclude = ["codigo_libro"]