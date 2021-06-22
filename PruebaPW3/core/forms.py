from django import forms
from django.forms import ModelForm
from .models import Libro

class LibroForm(ModelForm):
    model = Libro
    fields = ['ISBN','Titulo','Autor','Descripcion','Categoria',]