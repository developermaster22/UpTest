from django import forms
from .models import Producto, Caracteristicas
from django.forms import inlineformset_factory

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'disponible']

CaracteristicasFormSet = inlineformset_factory(
    Producto,
    Caracteristicas,
    fields=['nombre', 'valor'],
    extra=2,  #campos vacíos para agregar nuevas características
    can_delete=True
)
