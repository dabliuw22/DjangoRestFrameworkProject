from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_GET
from django.views.generic import CreateView, TemplateView
from django.core.urlresolvers import reverse_lazy

from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import viewsets, filters
from rest_framework.viewsets import ModelViewSet

import requests

from carrito.forms import CarritoForm

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

@require_GET
def producto_detail(request, producto_id):
    producto = get_object_or_404(Producto, id = producto_id)
    form = CarritoForm()
    return render(request, 'compras/producto_detail.html',
                  {'producto': producto, 'form': form})

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

    def create(self, request, *args, **kwargs):

        return super().create(request, *args, **kwargs)


class OrdenViewSet(ModelViewSet):
    queryset = Orden.objects.all()
    serializer_class = OrdenSerializer

    def create(self, request, *args, **kwargs):
        return super(OrdenViewSet, self).create(request, *args, **kwargs)

class ItemOrdenViewSet(ModelViewSet):
    queryset = ItemsOrden.objects.all()
    serializer_class = ItemsOrdenSerializer

# ------ Consumer API's --------

class OrdenConsumerView(TemplateView):
    template_name = 'compras/api_consumer.html'

    def get_context_data(self, **kwargs):
        context = super(OrdenConsumerView, self).get_context_data(**kwargs)
        response_json = requests.get('http://localhost:8000/api/orden/')
        if response_json.status_code == 200:
            context['json'] = response_json.json()
            for o in response_json.json():
                print(o)
        return context

class ProductoConsumerView(TemplateView):
    template_name = 'compras/api_consumer.html'

    def get_context_data(self, **kwargs):
        context = super(ProductoConsumerView, self).get_context_data(**kwargs)
        response_json = requests.get('http://localhost:8000/api/producto/')
        if response_json.status_code == 200:
            context['json'] = response_json.json()
            for p in response_json.json():
                print(p)
        return context

class ProductoConsumerAdd(CreateView):
    template_name = 'compras/producto_create.html'
    model = Producto
    form_class = ProductoForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['productos'] = Producto.objects.all().order_by('nombre')
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object
        if self.form_class(request.POST).is_valid():
            requests.post('http://localhost:8000/api/producto/',
                          {'nombre': request.POST['nombre'], 'precio': request.POST['precio']})
            return HttpResponseRedirect(reverse_lazy('compras:producto_consumer'))
        return self.render_to_response(self.get_context_data(form = self.form_class(request.POST)))

def producto_consumer_add(request):
    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            requests.post('http://localhost:8000/api/producto/',
                          {'nombre': request.POST['nombre'], 'precio': request.POST['precio']})
            return redirect('compras:producto_consumer')
    else:
        form = ProductoForm()
    return render(request, 'compras/producto_create.html',
                  {'form': form, 'productos': Producto.objects.all().order_by('nombre')})

def orden_consumer_add(request):
    pass