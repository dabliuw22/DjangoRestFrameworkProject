from django.shortcuts import render
from django.views.generic import CreateView
from django.core.urlresolvers import reverse_lazy

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.viewsets import ModelViewSet

from .models import Producto, Cliente, Orden, ItemsOrden
from .forms import ProductoForm, ClienteForm, OrdenForm
from .serializers import ClienteSerializer, ProductoSerializer, OrdenSerializer, ItemsOrdenSerializer

class ProductoCreate(CreateView):
    model = Producto
    form_class = ProductoForm
    template_name = 'compras/producto_create.html'
    success_url = reverse_lazy('compras:producto_create')

    def get_context_data(self, **kwargs):
        context = super(ProductoCreate, self).get_context_data(**kwargs)
        context['productos'] = Producto.objects.all().order_by('nombre')
        return context

class ClienteCreate(CreateView):
    model = Cliente
    form_class = ClienteForm
    template_name = 'compras/cliente_create.html'
    success_url = reverse_lazy('compras:orden_create')

    def get_context_data(self, **kwargs):
        context = super(ClienteCreate, self).get_context_data(**kwargs)
        context['clientes'] = Cliente.objects.all().order_by('email')
        return context

class OrdenCreate(CreateView):
    model = Orden
    form_class = OrdenForm
    template_name = 'compras/orden_create.html'
    success_url = reverse_lazy('index')

# ---------- API's -----------

class ClienteViewSet(ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = (DjangoFilterBackend, filters.OrderingFilter)
    filter_fields = ('email',)
    ordering_fields = ('email',)

class ProductoViewSet(ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    filter_backends = (filters.SearchFilter, filters.OrderingFilter)
    search_fields = ('nombre','precio')
    ordering_fields = ('nombre','precio')

class OrdenViewSet(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

class ItemOrdenViewSet(ModelViewSet):
    queryset = ItemsOrden.objects.all()
    serializer_class = ItemsOrdenSerializer