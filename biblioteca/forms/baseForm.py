from django import forms

class BaseModelForm(forms.ModelForm):
  template_name = "bs-form.html" 
  