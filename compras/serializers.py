from rest_framework import serializers

from .models import Cliente, Producto, Orden, ItemsOrden

class ClienteSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cliente
        fields = (
            'id',
            'email',
        )

class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = (
            'id',
            'nombre',
            'precio',
        )

class OrdenSerializer(serializers.ModelSerializer):
    total_orden = serializers.ReadOnlyField(source = 'get_total')
    fecha_hora = serializers.SerializerMethodField()
    cliente = ClienteSerializer()
    #productos = ProductoSerializer(many = True)
    items = serializers.SerializerMethodField()

    def get_fecha_hora(self, obj):
        return obj.fecha.strftime("%A, %d. %B %Y %I:%M%p")

    def get_items(self, obj):
        items = ItemsOrden.objects.filter(orden = obj)
        serializer = ItemsOrdenSerializer(data = items, many = True)
        serializer.is_valid()
        return serializer.data

    class Meta:
        model = Orden
        fields = (
            'id',
            'cliente',
            'fecha',
            'fecha_hora',
            'direccion',
            'estado',
            'items',
            'total_orden',
        )

class ItemsOrdenSerializer(serializers.ModelSerializer):
    producto = serializers.ReadOnlyField(source = 'producto.nombre')
    precio = serializers.ReadOnlyField(source = 'producto.precio')

    class Meta:
        model = ItemsOrden
        fields = (
            'producto',
            'precio',
            'precio_venta',
            'cantidad',
            'valor',
        )

