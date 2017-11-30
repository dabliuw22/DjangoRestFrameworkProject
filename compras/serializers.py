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

    def get_fecha_hora(self, obj):
        return obj.fecha.strftime("%A, %d. %B %Y %I:%M%p")

    class Meta:
        model = Orden
        fields = (
            'id',
            'cliente',
            'productos',
            'fecha',
            'fecha_hora',
            'direccion',
            'estado',
            'total_orden',
        )

class ItemsOrdenSerializer(serializers.ModelSerializer):

    class Meta:
        model = ItemsOrden
        fields = (
            'id',
            'orden',
            'producto',
            'precio_venta',
            'cantidad',
            'valor',
        )

