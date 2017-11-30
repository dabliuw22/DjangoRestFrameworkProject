import decimal

from functools import reduce

from django.db import models
from django.db.models.signals import post_save, pre_delete, post_delete
from django.dispatch import receiver
from django.utils import timezone

class Cliente(models.Model):
    email = models.EmailField()

    def __str__(self):
        return "{}".format(self.email)

class Producto(models.Model):
    nombre = models.CharField(max_length = 50)
    precio = models.DecimalField(max_digits = 8, decimal_places = 2)

    def __str__(self):
        return "{}".format(self.nombre)

class Orden(models.Model):
    OPCIONES_ESTADO = (
        ('PE', 'Pendiente'),
        ('OK', 'Suplida'),
    )

    cliente = models.ForeignKey(Cliente)
    productos = models.ManyToManyField(Producto, through = 'ItemsOrden', related_name = 'detalles_orden')
    fecha = models.DateTimeField()
    direccion = models.CharField(max_length = 50)
    estado = models.CharField(max_length = 15, choices = OPCIONES_ESTADO)
    total = models.DecimalField(default = 0.0, max_digits = 20, decimal_places = 2)

    def save(self, *args, **kwargs):
        self.fecha = timezone.now()
        self.total = self.get_total()
        super(Orden, self).save(*args, **kwargs)

    def get_total(self):
        items = ItemsOrden.objects.filter(orden = self)
        #result = ItemsOrden.objects.filter(orden = self).aggregate(total = models.Sum('valor'))
        #return result['total']
        return decimal.Decimal(reduce(lambda result, value: result + value,
                                      map(lambda v: decimal.Decimal(v.valor), items)))

    def __str__(self):
        return '{} - {}'.format(self.cliente, self.fecha)

class ItemsOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete = models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete = models.CASCADE)
    precio_venta = models.DecimalField(max_digits = 8, decimal_places = 2)
    cantidad = models.PositiveIntegerField(default = 0)
    valor = models.DecimalField(default = 0.0, max_digits = 20, decimal_places = 2)

    def save(self, *args, **kwargs):
        self.valor = self.precio_venta*self.cantidad
        super(ItemsOrden, self).save(*args, **kwargs)

@receiver(signal = pre_delete, sender = Orden)
def pre_delete_orden(sender, instance, **kwargs):
    items = ItemsOrden.objects.filter(orden = instance)
    for item in items:
        item.delete()

@receiver(signal = post_save, sender = ItemsOrden)
def post_save_item_save(sender, instance, created, **kwargs):
    instance.orden.save()

@receiver(signal = post_delete, sender = ItemsOrden)
def post_delete_item_delete(sender, instance, **kwargs):
    instance.orden.save()