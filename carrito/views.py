from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET

from .carrito import Carrito
from .forms import CarritoForm
from compras.models import Producto
# Create your views here.

@require_POST
def carrito_add(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id = producto_id)
    form = CarritoForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        carrito.add(producto = producto, cantidad = data['cantidad'],
                    update_cantidad = data['update_cantidad'])
    return redirect('carrito:carrito_detail')

def carrito_remove(request, producto_id):
    carrito = Carrito(request)
    producto = get_object_or_404(Producto, id=producto_id)
    carrito.remove(producto)
    return redirect('carrito:carrito_detail')

@require_GET
def carrito_detail(request):
    carrito = Carrito(request)
    for item in carrito:
        item['update_cantidad_form'] = CarritoForm(initial = {
            'cantidad': item['cantidad'],
            'update_cantidad': True
        })
    return render(request, 'carrito/carrito_detail.html', {'carrito': carrito})