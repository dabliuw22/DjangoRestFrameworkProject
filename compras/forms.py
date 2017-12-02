from django import forms

from .models import Producto, Cliente, Orden, ItemsOrden

class ProductoForm(forms.ModelForm):

    class Meta:
        model = Producto

        fields = (
            'nombre',
            'precio',
        )

        labels = {
            'nombre': 'Nombre',
            'precio': 'Precio',
        }

class ClienteForm(forms.ModelForm):

    class Meta:
        model = Cliente

        fields = (
            'email',
        )

        labels = {
            'email': 'E-mail',
        }

class OrdenForm(forms.ModelForm):

    class Meta:
        model = Orden

        fields = (
            'cliente',
            'direccion',
            'estado',
        )

        labels = {
            'cliente': 'Cliente',
            'direccion': 'Direccion',
            'estado': 'Estado',
        }

class ItemOrdenForm(forms.ModelForm):

    class Meta:
        model = ItemsOrden

        fields = (

        )