from django.http import Http404
from django.shortcuts import render, redirect

# Import Models
from ..models.editoriales import EditorialModel
from ..forms.editoriales import CrearEditorialesForm, EditarEditorialesForm

class EditorialesController:
    def listar(request):
        editoriales = EditorialModel.listarEditoriales()
        alert = request.session.pop('alert', None)
        return render(request, "editoriales/listar.html", { 'editoriales': editoriales, 'alert': alert})
    
    def agregar(request):
        form = CrearEditorialesForm()
        if request.method == 'POST':
            form = CrearEditorialesForm(request.POST)
            if form.is_valid():
                editorial = form.save(commit=False)
                if EditorialModel.insertarEditorial(editorial):
                    request.session['alert'] = { 'type': 'success', 'message': 'La editorial ha sido agregada exitosamente' }
                else:
                    request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al agregar la editorial' }
                return redirect('listarEditoriales')
        
        return render(request, "editoriales/agregar.html", { "form": form})

    def editar(request, codigo_editorial):
        editorial = EditorialModel.obtenerEditorial(codigo_editorial)
        if editorial:
            form = EditarEditorialesForm(instance=editorial)
            if request.method == 'POST':
                form = EditarEditorialesForm(request.POST, instance=editorial)
                if form.is_valid():
                    if EditorialModel.modificarEditorial(editorial):
                        request.session['alert'] = { 'type': 'success', 'message': 'La editorial ha sido actualizada exitosamente' }
                    else:
                        request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al actualizar la editorial' }
                    return redirect('listarEditoriales')
            
            return render(request, "editoriales/editar.html", { "editorial": editorial, "form": form})
        else:
            raise Http404("Editorial does not exist")
    
    def eliminar(request, codigo_editorial):
        if request.method == 'POST':
            editorial = EditorialModel.obtenerEditorial(codigo_editorial)
            if editorial:
                if EditorialModel.eliminarEditorial(editorial):
                    request.session['alert'] = { 'type': 'success', 'message': 'Le editorial ha sido eliminado exitosamente' }
                else:
                    request.session['alert'] = { 'type': 'error', 'message': 'Ha ocurrido un problema al eliminar la editorial' }

            return redirect('listarAutores')

