from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CaracteristicasFormSet


def lista_productos(request):
    productos = Producto.objects.prefetch_related('caracteristicas').all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = CaracteristicasFormSet(request.POST)
        if form.is_valid() and formset.is_valid():
            producto = form.save()
            formset.instance = producto
            formset.save()
            return redirect('lista_productos')
    else:
        form = ProductoForm()
        formset = CaracteristicasFormSet()

    return render(request, 'productos/agregar_productos.html', {
        'form': form,
        'formset': formset
    })
from django.shortcuts import get_object_or_404

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')


from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm, CaracteristicasFormSet

from django.shortcuts import render, get_object_or_404, redirect
from .models import Producto
from .forms import ProductoForm, CaracteristicasFormSet

def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        formset = CaracteristicasFormSet(request.POST, instance=producto)
        if producto_form.is_valid() and formset.is_valid():
            producto_form.save()
            formset.save()
            return redirect('lista_productos')
    else:
        producto_form = ProductoForm(instance=producto)
        formset = CaracteristicasFormSet(instance=producto)

    return render(request, 'productos/editar_productos.html', {
        'producto_form': producto_form,
        'formset': formset,
        'producto': producto,
    })
