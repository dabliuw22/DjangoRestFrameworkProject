from django.conf.urls import url

from .views import (ProductoCreate, ClienteCreate, OrdenCreate, ClienteViewSet,
                    OrdenConsumerView, ProductoConsumerView, ProductoConsumerAdd,
                    producto_detail)

urlpatterns = [
    url(r'^producto/add$', ProductoCreate.as_view(), name = 'producto_create'),
    url(r'^producto/(?P<producto_id>\d+)$', producto_detail, name = 'producto_detail'),
    url(r'^cliente/add$', ClienteCreate.as_view(), name = 'cliente_create'),
    url(r'^orden/add$', OrdenCreate.as_view(), name = 'orden_create'),
    #url(r'^api/cliente/list$', ClienteViewSet.as_view(), name = 'cliente_api_list')
    url(r'^orden/api/consumer$', OrdenConsumerView.as_view(), name = 'orden_consumer'),
    url(r'^orden/api/add', ProductoConsumerAdd.as_view(), name = 'api_add_orden'),
    url(r'^producto/api/consumer$', ProductoConsumerView.as_view(), name = 'producto_consumer'),
    url(r'^producto/api/add$', ProductoConsumerAdd.as_view(), name = "api_add_producto"),
]