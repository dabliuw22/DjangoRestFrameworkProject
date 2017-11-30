from django.contrib import admin

from compras.models import (Cliente, Producto, Orden, ItemsOrden)

class ClienteAdmin(admin.ModelAdmin):
    list_display = ('email',)

class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'precio')

class OrdenAdmin(admin.ModelAdmin):
    list_display = ('cliente', 'fecha', 'estado', 'total')

class ItemsOrdenAdmin(admin.ModelAdmin):
    list_display = ('orden', 'producto', 'cantidad', 'valor')

admin.site.register(Cliente, ClienteAdmin)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Orden, OrdenAdmin)
admin.site.register(ItemsOrden, ItemsOrdenAdmin)