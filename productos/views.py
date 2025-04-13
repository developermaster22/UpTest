from django.shortcuts import render, redirect
from .models import Producto
from .forms import ProductoForm, CaracteristicasFormSet
from django.shortcuts import get_object_or_404
from django.contrib import messages


def lista_productos(request):
    productos = Producto.objects.prefetch_related('caracteristicas').all()
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def agregar_producto(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        formset = CaracteristicasFormSet(request.POST)

        if form.is_valid() and formset.is_valid():
            producto = form.save()  # Guardar el producto

            # Asociar las características con el producto y guardarlas
            for form in formset:
                if form.cleaned_data:
                    caracteristica = form.save(commit=False)
                    caracteristica.producto = producto
                    caracteristica.save()

            messages.success(request, '¡Producto y características agregados correctamente!')
            return redirect('lista_productos')

    else:
        form = ProductoForm()
        formset = CaracteristicasFormSet()

    return render(request, 'productos/agregar_productos.html', {
        'form': form,
        'formset': formset,
    })

def eliminar_producto(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    producto.delete()
    return redirect('lista_productos')


def editar_producto(request, pk):
    producto = get_object_or_404(Producto, pk=pk)

    if request.method == 'POST':
        producto_form = ProductoForm(request.POST, instance=producto)
        formset = CaracteristicasFormSet(request.POST, instance=producto)

        if producto_form.is_valid() and formset.is_valid():
            producto = producto_form.save()  # Guardar producto
            formset.instance = producto      # Asociar el producto al formset
            formset.save()                   # Guardar características

            messages.success(request, '¡Producto actualizado correctamente!')
            return redirect('lista_productos')
        else:
            print("Errores en producto_form:", producto_form.errors)
            print("Errores en formset:", formset.errors)
            messages.error(request, 'Hubo un error al actualizar.')

    else:
        producto_form = ProductoForm(instance=producto)
        formset = CaracteristicasFormSet(instance=producto)

    return render(request, 'productos/editar_productos.html', {
        'producto_form': producto_form,
        'formset': formset,
        'producto': producto,
    })