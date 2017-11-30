from django.conf.urls import url

from .views import ProductoCreate, ClienteCreate, OrdenCreate, ClienteViewSet

urlpatterns = [
    url(r'^producto/add$', ProductoCreate.as_view(), name = 'producto_create'),
    url(r'^cliente/add$', ClienteCreate.as_view(), name = 'cliente_create'),
    url(r'^orden/add$', OrdenCreate.as_view(), name = 'orden_create'),
    #url(r'^api/cliente/list$', ClienteViewSet.as_view(), name = 'cliente_api_list')
]