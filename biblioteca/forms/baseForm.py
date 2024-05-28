from django import forms

class BaseModelForm(forms.ModelForm):
  template_name = "components/bs-form.html" 
  