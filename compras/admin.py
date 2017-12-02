from django.contrib import admin

from compras.models import (Cliente, Producto, Orden, ItemsOrden)

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email',)
    list_filter = ('email',)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')
    list_filter = ('precio',)
    list_editable = ('precio',)

@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'estado', 'total')
    search_fields = ['cliente__email']
    list_filter = ('estado',)
    list_editable = ('estado',)

@admin.register(ItemsOrden)
class ItemsOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'valor')