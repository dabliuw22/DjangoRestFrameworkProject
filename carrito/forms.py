from django import forms

class CarritoForm(forms.Form):
    CANTIDAD_PRODUCTO = [(i, str(i)) for i in range(1, 21)]
    cantidad = forms.TypedChoiceField(choices = CANTIDAD_PRODUCTO, coerce = int)
    update_cantidad = forms.BooleanField(required = False, initial = False, widget = forms.HiddenInput)